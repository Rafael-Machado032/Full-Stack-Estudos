"use client";
// frontend/app/analise/page.tsx
import dynamic from 'next/dynamic';
import React from 'react';
// Importa o componente Plot do react-plotly.js
const PlotClient = dynamic(() => import('./PlotClient'), { ssr: false });



async function AnaliseBitcoinPage() {
    let data = null;
    let error = null;

    try {
        const response = await fetch('http://127.0.0.1:8000/api/bitcoin/data', {
            cache: 'no-store' // Garante que sempre buscamos dados frescos);
        });
        if (!response.ok) {
            throw new Error('Falha ao buscar os dados da API.');
        }
        data = await response.json();
    } catch (err: any) {
        error = err.message;
    }

    // Se os dados foram carregados, preparamos os arrays para o gráfico
    const dates = data ? data.history.map((item: any) => item.date) : ["Nulo"];
    const prices = data ? data.history.map((item: any) => item.price_usd) : ["Nulo"];
    console.log(dates);
    

    // Configuração básica do gráfico de linha usando Plotly
    const plotData = [
        {
            x: dates,
            y: prices,
            type: 'scatter', // Tipo de gráfico: linha
            mode: 'lines+markers',
            marker: { color: 'rgb(0, 150, 136)' }, // Cor verde vibrante para Bitcoin
            name: 'Preço USD'
        }
    ];

    const layout = {
        title: 'Preço Histórico do Bitcoin (Últimos 7 dias)',
        xaxis: { title: 'Data/Hora' },
        yaxis: { title: 'Preço (USD)' },
        autosize: true,
        height: 500,
        margin: { t: 50, b: 50, l: 50, r: 50 }
    };

    return (
        <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
            <header>
                <h1>Dashboard de Análise de Bitcoin</h1>
                {data && (
                    <p>Preço Atual: <strong>${data.current_price.toFixed(2)} USD</strong> (Última atualização: {new Date(data.last_updated).toLocaleTimeString()})</p>
                )}
            </header>

            {error && <p style={{ color: 'red' }}>Erro: {error}</p>}

            {data ? (
                <div id="chart-container" style={{ marginTop: '20px' }}>
                    {/* Renderiza o gráfico usando o componente Plotly */}
                    <PlotClient
                        data={plotData as any} // 'as any' é um hack rápido para TypeScript, resolveremos isso depois
                        layout={layout as any}
                        style={{ width: '100%' }}
                    />
                    <p>ta certo</p>
                </div>
            ) : (
                <p>Carregando dados do back-end...</p>
            )}
        </div>
    );
}

export default AnaliseBitcoinPage;
