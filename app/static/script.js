document.addEventListener('DOMContentLoaded', () => {
    const questionsContainer = document.getElementById('questions-container')
    const form = document.getElementById('form')

    fetch('/api/questions')
        .then(response => response.json())
        .then(data => {
            data.questions.forEach(question => {
                const questionDiv = document.createElement('div');
                questionDiv.classList.add('question');
                questionDiv.innerHTML = `<h3>${question.text}</h3>`;

                question.choices.forEach(choice => {
                    const choiceInput = document.createElement('input');
                    choiceInput.type = 'radio';
                    choiceInput.name = `question_${question.id}`;
                    choiceInput.value = choice.id;

                    const choiceLabel = document.createElement('label');
                    choiceLabel.textContent = choice.text;

                    questionDiv.appendChild(choiceInput);
                    questionDiv.appendChild(choiceLabel);
                    questionDiv.appendChild(document.createElement('br'));
                });

                questionsContainer.appendChild(questionDiv);
            });
        });

    // form.addEventListener('submit', event => {
    //     event.preventDefault();
    //     const formData = new FormData(form);
    //     const choiceIds = Array.from(formData.values());

    //     fetch('/api/submit', {
    //         method: 'POST',
    //         headers: { 'Content-Type': 'application/json' },
    //         body: JSON.stringify({ choice_ids: choiceIds })
    //     })
    //     .then(response => response.json())
    //     .then(data => {
    //         window.location.href = `/results?submission_id=${data.submission_id}`;
    //     });
    // });
});

document.getElementById('quiz-form').addEventListener('submit', event => {
    event.preventDefault();

    const formData = new FormData(event.target);
    const choiceIds = Array.from(formData.values());

    fetch('/api/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ choice_ids: choiceIds })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = `/results?submission_id=${data.submission_id}`;
        } else {
            alert('There was an error submitting your quiz. Please try again.');
        }
    })
    .catch(error => console.error('Error submitting quiz:', error));
});