let builds = 0;

const botao = document.getElementById('btn');

botao.addEventListener('click', () => {
  builds++;
  botao.textContent = `${builds} ${builds === 1 ? 'build' : 'builds'} até agora`;
});
