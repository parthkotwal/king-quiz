document.addEventListener("DOMContentLoaded", () => {
    const questionContainer = document.getElementById("question-container");
    const prevButton = document.getElementById("prev-button");
    const nextButton = document.getElementById("next-button");
    const submitButton = document.getElementById("submit-button");

    let questions = [];
    let currentQuestionIndex = 0;
    const answers = {};

    // Fetch questions from the backend
    fetch("/api/questions")
        .then((response) => response.json())
        .then((data) => {
            questions = data.questions; // Assuming the API returns { questions: [...] }
            renderQuestion();
        })
        .catch((error) => console.error("Error fetching questions:", error));

    // Render the current question
    function renderQuestion() {
        const question = questions[currentQuestionIndex];
        questionContainer.innerHTML = `
            <h3>${question.text}</h3>
            ${question.choices
                .map(
                    (choice) => `
                <div class="choice" data-id="${choice.id}">
                    ${choice.text}
                </div>
            `
                )
                .join("")}
        `;

        // Highlight previously selected choice
        const selectedChoiceId = answers[question.id];
        if (selectedChoiceId) {
            const choiceElement = document.querySelector(
                `.choice[data-id="${selectedChoiceId}"]`
            );
            if (choiceElement) choiceElement.classList.add("selected");
        }

        addChoiceListeners();
        updateButtons();
    }

    // Add event listeners to choices
    function addChoiceListeners() {
        document.querySelectorAll(".choice").forEach((choice) => {
            choice.addEventListener("click", () => {
                // Deselect other choices and select the clicked one
                document.querySelectorAll(".choice").forEach((el) =>
                    el.classList.remove("selected")
                );
                choice.classList.add("selected");

                // Save the answer
                const questionId = questions[currentQuestionIndex].id;
                answers[questionId] = choice.dataset.id;

                updateButtons();
            });
        });
    }

    // Update navigation buttons
    function updateButtons() {
        prevButton.disabled = currentQuestionIndex === 0;
        nextButton.disabled =
            currentQuestionIndex === questions.length - 1 ||
            !answers[questions[currentQuestionIndex].id];
        submitButton.disabled = questions.some(
            (q) => !answers[q.id]
        );
    }

    // Navigation button logic
    prevButton.addEventListener("click", () => {
        if (currentQuestionIndex > 0) {
            currentQuestionIndex--;
            renderQuestion();
        }
    });

    nextButton.addEventListener("click", () => {
        if (
            currentQuestionIndex < questions.length - 1 &&
            answers[questions[currentQuestionIndex].id]
        ) {
            currentQuestionIndex++;
            renderQuestion();
        }
    });

    submitButton.addEventListener("click", () => {
        fetch("/api/submit", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ choice_ids: Object.values(answers) }),
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.submission_id) {
                    window.location.href = `/results?submission_id=${data.submission_id}`;
                } else {
                    alert("Error submitting quiz. Please try again.");
                }
            })
            .catch((error) => console.error("Error submitting quiz:", error));
    });
});
