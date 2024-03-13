import React, { useState, useEffect } from 'react';
import api from '../services/api';
import './styles.css';

function MovimentacaoEstoqueForm() {
    const [movimentacao, setMovimentacao] = useState({
        data_hora: '',
        mercadoria_id: 1,
        quantidade: 1,
        mercadoria_local_id: 1
    });
    const [mercadorias, setMercadorias] = useState([]);
    const [mercadoriaLocais, setMercadoriaLocais] = useState([]);
    const [mensagem, setMensagem] = useState('');

    useEffect(() => {
        carregarMercadorias();
        carregarMercadoriaLocais();
    }, []);

    const carregarMercadorias = () => {
        api.get('/mercadorias').then(response => {
            setMercadorias(response.data);
        });
    };

    const carregarMercadoriaLocais = () => {
        api.get('/mercadorias/locais').then(response => {
            setMercadoriaLocais(response.data);
        });
    };

    const handleChange = (e) => {
        setMovimentacao({ ...movimentacao, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
    
        const dadosFormatados = {
            ...movimentacao,
            mercadoria_id: parseInt(movimentacao.mercadoria_id),
            quantidade: parseInt(movimentacao.quantidade)
        };

        try {
            const response = await api.post(`/mercadorias/${movimentacao.mercadoria_id}/movimentacoes`, dadosFormatados);
            console.log(response.data);

            setMovimentacao({ data_hora: '', mercadoria_id: '', quantidade: 0, local: '' });
            setMensagem('Movimentação registrada com sucesso!');
            setTimeout(() => setMensagem(''), 5000);
        } catch (error) {
            console.error('Ocorreu um erro:', error);
            setMensagem('Falha ao registrar movimentação.');
            setTimeout(() => setMensagem(''), 5000);
        }
    };

    return (
        <div>
            {mensagem && <div>{mensagem}</div>}
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Data e Hora:</label>
                    <input
                        type="datetime-local"
                        name="data_hora"
                        value={movimentacao.data_hora}
                        onChange={handleChange}
                        required
                    />
                </div>
            
                <div>
                    <label>Mercadoria:</label>
                    <select
                        name="mercadoria_id"
                        value={movimentacao.mercadoria_id}
                        onChange={handleChange}
                        required
                    >
                        {mercadorias.map(mercadoria => (
                            <option key={mercadoria.id} value={mercadoria.id}>
                                {mercadoria.nome}
                            </option>
                        ))}
                    </select>
                </div>
            
                <div>
                    <label>Quantidade:</label>
                    <input
                        type="number"
                        name="quantidade"
                        value={movimentacao.quantidade}
                        onChange={handleChange}
                        required
                    />
                </div>
            
                <div>
                    <label>Local:</label>
                    <select
                        name="mercadoria_local_id"
                        value={movimentacao.mercadoria_local_id}
                        onChange={handleChange}
                        required
                    >
                        {mercadoriaLocais.map(mercadoriaLocal => (
                            <option key={mercadoriaLocal.id} value={mercadoriaLocal.id}>
                                {mercadoriaLocal.nome}
                            </option>
                        ))}
                    </select>
                </div>
            
                <button type="submit">Registrar Movimentação</button>
            </form>
        </div>
    );
}

export default MovimentacaoEstoqueForm;
