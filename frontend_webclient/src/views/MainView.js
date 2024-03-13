import React, { useState } from 'react';
import MovimentacaoEstoqueForm from '../components/MovimentacaoEstoqueForm';
import EstoqueGrafico from '../components/EstoqueGrafico';
import MercadoriasList from '../components/MercadoriasList'; // Importe seu componente

function MainView() {
    const [activeTab, setActiveTab] = useState('mercadorias');

    const buttonStyle = {
        margin: '0 10px 20px 0', // Adiciona margem à direita e abaixo dos botões
        padding: '10px',          // Adiciona um pouco de preenchimento interno para os botões
    };

    return (
        <div>
            <h3>Listagens e Cadastros</h3>
            <button style={buttonStyle} onClick={() => setActiveTab('mercadorias')}>
                Mercadorias
            </button>
            <button style={buttonStyle} onClick={() => setActiveTab('mercadorias')}>
                Fabricantes
            </button>
            <button style={buttonStyle} onClick={() => setActiveTab('mercadorias')}>
                Tipos de Mercadoria
            </button>
            <button style={buttonStyle} onClick={() => setActiveTab('mercadorias')}>
                Locais de Mercadoria
            </button>
            <br/><br/>
            <button style={buttonStyle} onClick={() => setActiveTab('movimentacao')}>
                Movimentação de Mercadorias
            </button>
            <button style={buttonStyle} onClick={() => setActiveTab('relatorio')}>
                Relatório dos Totais
            </button>
            
            {activeTab === 'mercadorias' && <MercadoriasList />}
            {activeTab === 'movimentacao' && <MovimentacaoEstoqueForm />}
            {activeTab === 'relatorio' && <EstoqueGrafico />}
        </div>
    );
}

export default MainView;
