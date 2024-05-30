
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('aparecer');
        }
    })
})

const hiddenElements = document.querySelectorAll('.container-info');
hiddenElements.forEach((el => observer.observe(el)))