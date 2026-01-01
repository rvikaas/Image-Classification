async function predictImage(file) {
    
    const formdata = new FormData();

    formdata.append("file",file)

    const response = await fetch("http://localhost:8000/api/predict", {
    method: "POST",
    body: formdata,
  });

  if (!response.ok) {
    throw new Error("Prediction failed");
  }

  return await response.json();
    
}

export default predictImage 