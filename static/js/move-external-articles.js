document.addEventListener("DOMContentLoaded", function() {
  var jsonUrl = '/prev_articles.json';

  function toDate(rawDate) {
    return new Date(rawDate).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })
  }

  fetch(jsonUrl)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok ' + response.statusText);
      }
      return response.json();
    })
    .then(articles => {
      var externalArticlesHTML = `
      <section id="external-articles" class="external-articles">
        <h2>Previous articles:</h2><br/>
        ${articles.map(article => {
          // Handle Medium articles
          if (article.guid) {
            return `
              <article class="post-entry">
                  <figure class="entry-cover">
                      ${article.thumbnail ? `<img loading="lazy" src="${article.thumbnail}" height="250px" alt="${article.title}">` : ''}
                  </figure>
                  <header class="entry-header">
                      <h2 class="entry-hint-parent">${article.title}</h2>
                  </header>
                  <div class="entry-content">
                      <p>${article.description.substring(0, 189)}${article.description.length > 189 ? '...' : ''}</p>
              </div>
              <footer class="entry-footer">
                  <span title="${toDate(article.pubDate)}">${toDate(article.pubDate)}</span>&nbsp;·&nbsp;${article.author}
              </footer>
                  <a class="entry-link" aria-label="post link to ${article.title}" href="${article.link}" target="_blank"></a>
              </article>
            `;
          }
          // Handle Dev.to articles
          else if (article.type_of === "article") {
            return `
              <article class="post-entry">
                  <figure class="entry-cover">
                      ${article.cover_image ? `<img loading="lazy" src="${article.cover_image}" height="250px" alt="${article.title}">` : ''}
                  </figure>
                  <header class="entry-header">
                      <h2 class="entry-hint-parent">${article.title}</h2>
                  </header>
                  <div class="entry-content">
                      <p>${article.description.substring(0, 200)}${article.description.length > 200 ? '...' : ''}</p>
              </div>
              <footer class="entry-footer">
                  <span title="${toDate(article.published_timestamp)}">${toDate(article.published_timestamp)}</span>&nbsp;·&nbsp;${article.user.name}
              </footer>
                  <a class="entry-link" aria-label="post link to ${article.title}" href="${article.url}" target="_blank"></a>
              </article>
            `;
          }
        }).join('')}
      </section>
      `;

      var postEntries = document.getElementsByClassName("post-entry");
      var mainContent = postEntries[postEntries.length - 1];
      if (mainContent) {
        var tempDiv = document.createElement('div');
        tempDiv.innerHTML = externalArticlesHTML;
        var externalArticlesElement = tempDiv.firstElementChild;
        mainContent.insertAdjacentElement('afterend', externalArticlesElement);
      }
    })
    .catch(error => console.error('Error fetching articles:', error));
});