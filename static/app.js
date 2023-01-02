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
        </div>
      ))}
    </div>
  );
};

export default GistFinder;
