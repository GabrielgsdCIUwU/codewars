import axios from 'axios';
import fs from 'fs';
import path from 'path';

const languageExtensions = {
    python: 'py',
    java: 'java',
    javascript: 'js',
};

const rootFolder = './';

async function fetchCompletedChallenges() {
    let page = 0;
    let totalPages = 1;
    const readmeData = {};

    while (page < totalPages) {
        try {
            const response = await axios.get(`https://www.codewars.com/api/v1/users/GabrielgsdCIUwU/code-challenges/completed?page=${page}`);
            const { totalPages: fetchedTotalPages, data } = response.data;

            totalPages = fetchedTotalPages;

            for (const item of data) {
                const language = item.completedLanguages[0];
                const extension = languageExtensions[language] || language;
                const folderPath = path.join(process.cwd(), language, item.slug);

                if (!fs.existsSync(folderPath)) {
                    fs.mkdirSync(folderPath, { recursive: true });

                    const urlFilePath = path.join(folderPath, 'url.txt');
                    fs.writeFileSync(urlFilePath, item.id, 'utf8');

                    const solutionFilePath = path.join(folderPath, `solution.${extension}`);
                    fs.writeFileSync(solutionFilePath, '', 'utf8');
                }

                if (!readmeData[language]) {
                    readmeData[language] = [];
                }
                readmeData[language].push({ name: item.name, link: `./${language}/${item.slug}` });

                // Verificar si el README ya existe antes de generar uno nuevo
                const kataReadmePath = path.join(folderPath, 'README.md');
                if (!fs.existsSync(kataReadmePath)) {
                    await generateKataReadme(folderPath, item.slug);
                }

            }

            page++;
        } catch (error) {
            console.error(`Error fetching or processing page ${page}:`, error.message);
            break;
        }
    }

    generateMainReadme(readmeData);
}

async function generateKataReadme(folderPath, slug) {
    const kataUrl = `https://www.codewars.com/api/v1/code-challenges/${slug}`;

    try {
        const response = await axios.get(kataUrl);
        if (response.status === 200) {
            const data = response.data;
            const title = data.name;
            const description = data.description;
            const createdBy = data.createdBy.username;
            const publishedAt = new Date(data.publishedAt).toLocaleDateString();
            const kataUrl = data.url;

            const readmeContent = `# ${title}
${description}

## Información del Kata realizado:
Creado por: ${createdBy}

Publicado el: ${publishedAt}

URL: [Haz click aquí para ir al Kata](${kataUrl})`;

            fs.writeFileSync(path.join(folderPath, 'README.md'), readmeContent);
            console.log(`README.md creado para ${title}`);
        } else {
            console.error('No se pudo obtener la descripción del kata.');
        }
    } catch (error) {
        console.error('Error al hacer la solicitud:', error.message);
    }
}

function generateMainReadme(readmeData) {
    const readmeHeader = `# Ejercicios Codewars

Bienvenido al repositorio de ejercicios de CodeWars realizados por Gabrielgsd. Aquí encontrarás una recopilación de soluciones a los desafíos completados en la plataforma, organizadas por lenguaje de programación.

Cada ejercicio incluye:
- Una carpeta específica con su solución.
- Un archivo que contiene su ID único.

A continuación, encontrarás una lista de los katas organizados por lenguaje de programación:

`;

    const readmeContent = Object.keys(readmeData)
        .sort()
        .map(language => {
            const sortedKatas = readmeData[language]
                .sort((a, b) => a.name.localeCompare(b.name))
                .map(kata => `- [${kata.name}](${kata.link})`)
                .join('\n');
            return `# ${language.charAt(0).toUpperCase() + language.slice(1)}\n${sortedKatas}`;
        })
        .join('\n\n');

    fs.writeFileSync(path.join(process.cwd(), 'README.md'), readmeHeader + readmeContent, 'utf8');
    console.log('README.md principal creado.');
}

fetchCompletedChallenges();
