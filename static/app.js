import React from "react";

const GistFinder = ({ gists }) => {
  return (
    <div>
      {gists.map((gist) => (
        <div key={gist.id} className="gist">
          <h2>{gist.description}</h2>
          {gist.files.map((file) => (
            <span key={file.filename} className="badge">{file.type}</span>
          ))}
          <h3>Forks:</h3>
          <ul>
            {gist.forks.map((fork) => (
              <li key={fork.id}>
                <img src={fork.user.avatar_url} alt={fork.user.login} className="avatar" />
                {fork.user.login}
              </li>
            ))}
          </ul>
          <a href={`/gist/${gist.id}`}>View Gist</a>
        </div>
      ))}
    </div>
  );
};

export default GistFinder;

