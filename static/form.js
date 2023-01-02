import React from 'react';

const GistForm = ({ onSubmit }) => {
  return (
    <form onSubmit={onSubmit}>
      <label htmlFor="gistId">
        Gist ID:
        <input type="text" name="gistId" />
      </label>
      <button type="submit">Submit</button>
    </form>
  );
};

export default GistForm;
