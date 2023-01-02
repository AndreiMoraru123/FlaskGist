import React from 'react';

const Gist = ({ description, files }) => {
  return (
    <div>
      <h1>{description}</h1>
      {files.map((file) => (
        <div key={file.id}>
          <h2>{file.filename}</h2>
          <pre>{file.content}</pre>
        </div>
      ))}
    </div>
  );
};

export default Gist;
