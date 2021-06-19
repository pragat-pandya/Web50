document.addEventListener('DOMContentLoaded', function () {
    // Collecting DOM objects as JS variables for ease of reference
    const sumbit = document.querySelector('#submit');
    const newTask = document.querySelector('#task');

    // By default submit button is disabled.
    sumbit.disabled = true;
    
    // When user types something in #task(newTask). Enable the submit button.
    newTask.onkeyup = () => {
        if (newTask.value.length > 0) sumbit.disabled = false;
        else sumbit.disabled = true;
    };

    // Listne for submission of the form.
    document.querySelector('form').onsubmit = () => {
        const task = newTask.value;
        const li = document.createElement('li');
        li.innerHTML = task;
        document.querySelector('#tasks').append(li);

        // cleat out input field
        newTask.value = '';

        //disable the submit button again
        sumbit.disabled = true;

        // Stop from form submission
        return false;
    }
});