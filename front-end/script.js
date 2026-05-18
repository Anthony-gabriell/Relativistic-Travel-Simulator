async function calculate() {
    const destine = document.getElementById('destination').value;
    const velocity = document.getElementById('velocity').value;

    const response = await fetch('http://127.0.0.1:5000/calculate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ destine: destine, velocity: velocity })
    });

    const data = await response.json();

    if (data.error) {
        alert(data.error);
        return;
    }

    document.getElementById('lorentz').textContent = data.lorentz_factor.toFixed(4);
    document.getElementById('time_earth').textContent = data.time_on_earth.toFixed(2) + ' years';
    document.getElementById('time_traveler').textContent = data.time_for_traveler.toFixed(2) + ' years';
    document.getElementById('contracted').textContent = data.contracted_distance.toFixed(4) + ' light-years';
    document.getElementById('energy').textContent = data.relativistic_energy.toExponential(2) + ' J';

    document.getElementById('results').style.display = 'block';
}