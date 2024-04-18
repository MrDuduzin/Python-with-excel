# Eduardo Enzo Pedro de Melo - 16/04/2024
from os import system
import pandas as pd

dadosPessoais = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Luiza', 'Carlos', 'Laura', 'Felipe', 'Juliana', 'Rafael', 'Fernanda', 'Rodrigo', 'Aline', 'Gustavo', 'Camila', 'Diego', 'Carolina', 'Lucas', 'Bianca', 'Marcela', 'Mariana', 'Thiago', 'Isabela', 'Henrique', 'Natália', 'Gabriel', 'Larissa', 'Bruno', 'Amanda', 'Paulo'],
    
    'Sobrenome': ['Silva', 'Santos', 'Oliveira', 'Pereira', 'Almeida', 'Ferreira', 'Costa', 'Rodrigues', 'Martins', 'Carvalho', 'Gomes', 'Alves', 'Lima', 'Araújo', 'Barbosa', 'Rocha', 'Melo', 'Sousa', 'Nascimento', 'Souza', 'Cavalcanti', 'Ribeiro', 'Monteiro', 'Mendes', 'Dias', 'Castro', 'Cardoso', 'Correia', 'Nunes', 'Pinto'],
    
    'Data de nascimento': ['01/01/1990', '02/02/1991', '03/03/1992', '04/04/1993', '05/05/1994', '06/06/1995', '07/07/1996', '08/08/1997', '09/09/1998', '10/10/1999', '11/11/2000', '12/12/2001', '13/01/2002', '14/02/2003', '15/03/2004', '16/04/2005', '17/05/2006', '18/06/2007', '19/07/2008', '20/08/2009', '21/09/2010', '22/10/2011', '23/11/2012', '24/12/2013', '25/01/2014', '26/02/2015', '27/03/2016', '28/04/2017', '29/05/2018', '30/06/2019'],
    
    'Graduação': ['Administração', 'Engenharia', 'Medicina', 'Direito', 'Psicologia', 'Economia', 'Biologia', 'Arquitetura', 'Ciências Contábeis', 'Comunicação Social', 'Física', 'Química', 'Letras', 'História', 'Geografia', 'Matemática', 'Educação Física', 'Nutrição', 'Farmácia', 'Odontologia', 'Artes', 'Design', 'Informática', 'Turismo', 'Gastronomia', 'Enfermagem', 'Veterinária', 'Pedagogia', 'Sociologia', 'Filosofia'],
    
    'Universidade cursada': ['USP', 'UNESP', 'UNICAMP', 'UFMG', 'UFRJ', 'UFSC', 'UFRGS', 'UFPE', 'UNB', 'UNIFESP', 'UFF', 'PUC-RJ', 'PUC-SP', 'UFBA', 'UFPR', 'UFRN', 'UNIFOR', 'UFES', 'UNICAP', 'UFMA', 'UEL', 'UEM', 'UNIMAR', 'UNIFOR', 'UNICEUB', 'UNINOVE', 'UNISINOS', 'UNIVALI', 'UFG', 'UFSCar'],
    
    'Ano de graduação': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039],
    
    'Área de atuação': ['Marketing', 'Engenharia Civil', 'Pediatria', 'Advocacia', 'Recursos Humanos', 'Educação', 'Genética', 'Urbanismo', 'Auditoria', 'Jornalismo', 'Pesquisa', 'Farmácia Hospitalar', 'Tradução', 'Arqueologia', 'Planejamento Urbano', 'Ensino Médio', 'Consultoria', 'Alimentação', 'Estética', 'Periodontia', 'Dança', 'Web Design', 'Hotelaria', 'Nutrição Clínica', 'Oncologia', 'Zootecnia', 'Educação Infantil', 'Assistência Social', 'Ética Profissional', 'Filosofia Política']
}

df = pd.DataFrame(dadosPessoais)
print(df)


def converter():
    conversor = df.to_excel('Tabela Projeto.xlsx', index=False)
    return conversor
converter()