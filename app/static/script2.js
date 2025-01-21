document.addEventListener("DOMContentLoaded", () => {
    const questionContainer = document.getElementById("question-container");
    const prevButton = document.getElementById("prev-button");
    const nextButton = document.getElementById("next-button");
    const submitButton = document.getElementById("submit-button");
    const progressFill = document.getElementById("progress-fill");
    const currentQuestionSpan = document.getElementById("current-question");
    const totalQuestionsSpan = document.getElementById("total-questions");
    const loadingOverlay = document.getElementById("loading-overlay");

    let questions = [];
    let currentQuestionIndex = 0;
    const answers = {};

    function showLoading() {
        loadingOverlay.style.display = "flex";
    }

    function hideLoading() {
        loadingOverlay.style.display = "none";
    }

    // Fetch questions from the backend
    showLoading();
    fetch("/api/questions")
        .then((response) => response.json())
        .then((data) => {
            questions = data.questions;
            totalQuestionsSpan.textContent = questions.length;
            renderQuestion();
            hideLoading();
        })
        .catch((error) => {
            console.error("Error fetching questions:", error);
            hideLoading();
            alert("Error loading quiz questions. Please try again.");
        });

    // Update progress bar
    function updateProgress() {
        const progress = ((currentQuestionIndex + 1) / questions.length) * 100;
        progressFill.style.width = `${progress}%`;
        currentQuestionSpan.textContent = currentQuestionIndex + 1;
    }

    // Render the current question with animation
    function renderQuestion() {
        const question = questions[currentQuestionIndex];
        
        // Fade out current content
        questionContainer.style.opacity = "0";
        
        setTimeout(() => {
            questionContainer.innerHTML = `
                <h3>${question.text}</h3>
                <div class="choices-container">
                    ${question.choices
                        .map(
                            (choice) => `
                        <div class="choice" data-id="${choice.id}">
                            ${choice.text}
                        </div>
                    `
                        )
                        .join("")}
                </div>
            `;

            // Highlight previously selected choice
            const selectedChoiceId = answers[question.id];
            if (selectedChoiceId) {
                const choiceElement = document.querySelector(
                    `.choice[data-id="${selectedChoiceId}"]`
                );
                if (choiceElement) choiceElement.classList.add("selected");
            }

            // Fade in new content
            setTimeout(() => {
                questionContainer.style.opacity = "1";
            }, 50);

            addChoiceListeners();
            updateButtons();
            updateProgress();
        }, 300);
    }

    // Add event listeners to choices with improved feedback
    function addChoiceListeners() {
        document.querySelectorAll(".choice").forEach((choice) => {
            choice.addEventListener("click", () => {
                // Add ripple effect
                const ripple = document.createElement("div");
                ripple.classList.add("ripple");
                choice.appendChild(ripple);
                setTimeout(() => ripple.remove(), 600);

                // Deselect other choices and select the clicked one
                document.querySelectorAll(".choice").forEach((el) =>
                    el.classList.remove("selected")
                );
                choice.classList.add("selected");

                // Save the answer
                const questionId = questions[currentQuestionIndex].id;
                answers[questionId] = choice.dataset.id;

                updateButtons();

                // Auto-advance to next question after short delay
                if (currentQuestionIndex < questions.length - 1) {
                    setTimeout(() => {
                        nextButton.click();
                    }, 500);
                }
            });
        });
    }

    // Update navigation buttons with improved logic
    function updateButtons() {
        prevButton.disabled = currentQuestionIndex === 0;
        nextButton.disabled =
            currentQuestionIndex === questions.length - 1 ||
            !answers[questions[currentQuestionIndex].id];
        
        // Enable submit only if all questions are answered
        const allAnswered = questions.every((q) => answers[q.id]);
        submitButton.disabled = !allAnswered;
        
        if (allAnswered) {
            submitButton.classList.add("pulse");
        } else {
            submitButton.classList.remove("pulse");
        }
    }

    // Navigation button logic with smooth transitions
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
        showLoading();
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
                    hideLoading();
                    alert("Error submitting quiz. Please try again.");
                }
            })
            .catch((error) => {
                console.error("Error submitting quiz:", error);
                hideLoading();
                alert("Error submitting quiz. Please try again.");
            });
    });
});