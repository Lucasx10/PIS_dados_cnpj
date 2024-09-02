function renderiza_uf(url) {
    fetch(url, {
        method: 'get',
    }).then(function(result) {
        return result.json();
    }).then(function(data) {
        const ctx = document.getElementById('relatorio_uf').getContext('2d');

        const total = data.data.reduce((sum, value) => sum + value, 0);
        const percentages = data.data.map(value => (value / total * 100).toFixed(1) + '%');
        const labels = data.labels;

        // Cores pré-definidas
        const predefinedColors = [
            'rgb(0, 123, 255)', // Azul
            'rgb(255, 193, 7)', // Amarelo
            'rgb(40, 167, 69)', // Verde
            'rgb(255, 87, 34)'  // Laranja
        ];

        // Garante que cada UF receba uma cor do conjunto
        const backgroundColors = labels.map((_, index) => predefinedColors[index % predefinedColors.length]);

        const myChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: labels,
                datasets: [{
                    data: data.data,
                    backgroundColor: backgroundColors,
                    hoverOffset: 4
                }]
            },
            options: {
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function(tooltipItem) {
                                const label = tooltipItem.label || '';
                                const value = tooltipItem.raw || 0;
                                const percentage = percentages[tooltipItem.dataIndex] || '0%';
                                return `${label}: ${value} (${percentage})`;
                            }
                        }
                    },
                    legend: {
                        display: false // Desativa a legenda padrão
                    }
                }
            }
        });

        // Adiciona a legenda personalizada
        const legendContainer = document.getElementById('legend-container');
        legendContainer.innerHTML = '';
        labels.forEach((label, index) => {
            const percentage = percentages[index];
            const color = backgroundColors[index];
            legendContainer.innerHTML += `<i style="color: ${color};" class="fa fa-circle"></i><span>${label}: ${percentage} </span>`;
        });
    });
}


function renderiza_data(url) {
    fetch(url, {
        method: 'get',
    }).then(function(result) {
        return result.json();
    }).then(function(data) {
        const ctx = document.getElementById('relatorio_data').getContext('2d');

        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Data inicio Atividades',
                    data: data.data,
                    borderColor: 'rgb(245, 58, 58)',
                    backgroundColor: 'rgb(245, 58, 58, 0.2)',
                    fill: false,
                    tension: 0.1
                }]
            },
            options: {
                scales: {
                    y: {
                        ticks: {
                            // Define a formatação dos ticks como inteiros
                            callback: function(value) {
                                return Number.isInteger(value) ? value : '';
                            }
                        }
                    }
                }
            }
        });

        // Encontra o índice do valor máximo
        const maxValue = Math.max(...data.data);
        const maxIndex = data.data.indexOf(maxValue);
        const maxLabel = data.labels[maxIndex];

        // Adiciona a legenda personalizada para o valor máximo
        const legendContainer = document.getElementById('legend-container2');
        legendContainer.innerHTML = '';
        const color = myChart.data.datasets[0].borderColor;
        legendContainer.innerHTML = `<i style="color: ${color};" class="fa fa-circle"></i><span>${maxLabel}: ${maxValue}</span>`;
    });
}
