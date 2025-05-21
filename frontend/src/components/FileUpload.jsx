import axios from "axios";

export default function FileUpload({ onUploadSuccess }) {
  const handleUpload = async (e) => {
    const formData = new FormData();
    formData.append("file", e.target.files[0]);
    await axios.post("http://localhost:5000/upload", formData);
    onUploadSuccess();
  };

  return <input type="file" onChange={handleUpload} />;
}
