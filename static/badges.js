import React from 'react';

function Badges(props) {
  return (
    <div>
      {props.fileTypes.map(fileType => (
        <span className="badge">{fileType}</span>
      ))}
    </div>
  );
}

export default Badges;
