import { useState } from "react";
import "./App.css";
import ChatUi from "./components/ChatUI";
import FileUpload from "./components/FileUpload";

function App() {
  return (
    <>
      <div className="flex flex-col items-center">
        <p className=" text-3xl">Ask Your Docs</p>
        <ChatUi />
      </div>
    </>
  );
}

export default App;
