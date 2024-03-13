import React, { useState, useEffect } from 'react';
import api from '../services/api';
import './styles.css';


function MercadoriaForm({ mercadoria, onSave, onCancel }) {
  const mercadoriaId = mercadoria.id || 0;
  const [dadosFormulario, setDadosFormulario] = useState({
    nome: mercadoria.nome || '',
    numero_registro: mercadoria.numero_registro || '',
    fabricante_id: mercadoria.fabricante_id || '',
    mercadoria_tipo_id: mercadoria.mercadoria_tipo_id || '',
    descricao: mercadoria.descricao || ''
  });
  const [fabricantes, setFabricantes] = useState([]);
  const [mercadoriaTipos, setMercadoriaTipos] = useState([]);
  const [mensagem, setMensagem] = useState('');
  
  useEffect(() => {
      carregarFabricantes();
      carregarMercadoriaTipos();
  }, []);

  const carregarFabricantes = () => {
      api.get('/fabricantes').then(response => {
          setFabricantes(response.data);
      });
  };

  const carregarMercadoriaTipos = () => {
      api.get('/mercadorias/tipos').then(response => {
          setMercadoriaTipos(response.data);
      });
  };

  const handleChange = (e) => {
    setDadosFormulario({ ...dadosFormulario, [e.target.name]: e.target.value });
  };
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      if (mercadoriaId) {
        const response = await api.put(`/mercadorias/${mercadoriaId}`, dadosFormulario);
        console.log(response.data);
        setMensagem('Mercadoria editada com sucesso!');
      } else {
        const response = await api.post('/mercadorias', dadosFormulario);
        console.log(response.data);
        setMensagem('Mercadoria adicionada com sucesso!');
      }
      setTimeout(() => setMensagem(''), 5000);
      onSave(); // Chame onSave para informar ao componente pai que a operação foi concluída
    } catch (error) {
      console.error('Ocorreu um erro ao enviar os dados:', error);
      setMensagem('Falha ao adicionar mercadoria.');
      setTimeout(() => setMensagem(''), 5000); // Limpa a mensagem após 5 segundos
    }
  };
  
  return (
    <div>
      {mensagem && <div>{mensagem}</div>}
      <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="nome">Nome:</label>
            <input
              type="text"
              name="nome"
              value={dadosFormulario.nome}
              onChange={handleChange}
              required
            />
          </div>

          <div>
            <label>Número de Registro:</label>
            <input
              type="text"
              name="numero_registro"
              value={dadosFormulario.numero_registro}
              onChange={handleChange}
              required
            />
          </div>

          <div>
            <label>Fabricante:</label>
            <select
                name="fabricante_id"
                value={dadosFormulario.fabricante_id}
                onChange={handleChange}
                required
            >
                {fabricantes.map(fabricante => (
                    <option key={fabricante.id} value={fabricante.id}>
                        {fabricante.nome}
                    </option>
                ))}
            </select>
          </div>

          <div>
            <label>Tipo:</label>
            <select
                name="mercadoria_tipo_id"
                value={dadosFormulario.mercadoria_tipo_id}
                onChange={handleChange}
                required
            >
                {mercadoriaTipos.map(mercadoriaTipo => (
                    <option key={mercadoriaTipo.id} value={mercadoriaTipo.id}>
                        {mercadoriaTipo.nome}
                    </option>
                ))}
            </select>
          </div>

          <div>
            <label>Descrição:</label>
            <textarea
              name="descricao"
              value={dadosFormulario.descricao}
              onChange={handleChange}
              required
            />
          </div>
          <button type="submit">{mercadoriaId ? 'Salvar Mercadoria' : 'Inserir Nova Mercadoria'}</button>
          <button type="button" onClick={onCancel} style={{ marginLeft: '10px' }}>Cancelar</button>
           
        </form>
    </div>
  );
}

export default MercadoriaForm;
