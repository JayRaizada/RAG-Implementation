import axios from "axios";
import { useState } from "react";
import ReactMarkdown from "react-markdown";
import uploadIcon from "../images/attach-file.png";

export default function ChatUI() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [prevChats, setPrevChats] = useState("");

  const handleAsk = async () => {
    const res = await axios.post("http://localhost:5000/query", {
      question: query,
    });
    setResponse(res.data.answer.result);
    console.log(res.data.answer.result);
  };

  const handleUpload = async (e) => {
    const formData = new FormData();
    formData.append("file", e.target.files[0]);
    await axios.post("http://localhost:5000/upload", formData);
    onUploadSuccess();
  };

  return (
    <div className="flex flex-col mb-4">
      <div className="w-screen p-24 h-[76vh] overflow-auto">
        <ReactMarkdown>{response}</ReactMarkdown>
      </div>
      <div className="flex items-center justify-center">
        <div>
          <input
            id="file-upload"
            type="file"
            onChange={handleUpload}
            className="hidden "
          />
          <label htmlFor="file-upload" className="cursor-pointer ">
            <img
              src={uploadIcon}
              alt="Upload"
              className="w-8 h-8"
            />
          </label>
        </div>
        <input
          className=" border-white border-2 rounded-3xl px-4 py-2 mx-4 w-[60vw]"
          placeholder="type your query here!"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button onClick={handleAsk}>Ask</button>
      </div>
    </div>
  );
}
