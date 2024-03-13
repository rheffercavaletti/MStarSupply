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
            <button style={buttonStyle} onClick={() => setActiveTab('mercadorias')}>
                Gerenciamento de Mercadorias
            </button>
            <button style={buttonStyle} onClick={() => setActiveTab('movimentacao')}>
                Movimentação de Estoque
            </button>
            <button style={buttonStyle} onClick={() => setActiveTab('relatorio')}>
                Gráfico de Estoque
            </button>
            
            {activeTab === 'mercadorias' && <MercadoriasList />}
            {activeTab === 'movimentacao' && <MovimentacaoEstoqueForm />}
            {activeTab === 'relatorio' && <EstoqueGrafico />}
        </div>
    );
}

export default MainView;
