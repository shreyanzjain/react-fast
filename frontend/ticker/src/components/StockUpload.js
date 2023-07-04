import React, { useRef, useState } from "react";
import StockDisplay from "./StockDisplay";

function StockUpload() {
  const fileInput = useRef();

  const [isShown, setIsShown] = useState(false);

  const handleClick = () => {
    setIsShown(!isShown);
  };

  const uploadFile = () => {
    const file = fileInput.current.files[0];
    const formData = new FormData();
    formData.append("file", file);

    fetch("http://localhost:8000/data/upload", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.error(error));
  };

  return (
    <div className="row-col">
      <div className="card col-4 mt-3 mb-3 me-3">
        <div className="card-body">
          <input className="btn" type="file" ref={fileInput} />
          <button className="btn btn-outline-dark" onClick={uploadFile}>
            Upload
          </button>
        </div>
      </div>
      <div className="card col-4 mt-3 mb-3">
        <div className="card-body">
          <button className="btn btn-outline-dark" onClick={handleClick}>
            GET FILES
          </button>
        </div>
      </div>
      <div>{isShown && <StockDisplay />}</div>
    </div>
  );
}

export default StockUpload;
