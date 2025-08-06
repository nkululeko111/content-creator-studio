from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/videos")
def get_videos():
    return jsonify([
        {"title": "Kenny Kunene EXPOSED", "status": "uploaded"},
        {"title": "Beyoncé Cape Town Scandal", "status": "pending"}
    ])

if __name__ == "__main__":
    app.run(debug=True)






#     import React, { useState, useEffect } from 'react';

# function App() {
#   const categories = [
#     "News & Gossip",
#     "Conspiracies",
#     "Life Hacks",
#     "Sports",
#     "Technology",
#     "Kids Education",
#     "Untold Stories",
#     "Folktales",
#     "Music"
#   ];

#   const [topics, setTopics] = useState({});
#   const [status, setStatus] = useState({}); // track process status

#   // Fetch topics
#   useEffect(() => {
#     categories.forEach(cat => {
#       fetch(`/api/topics/${encodeURIComponent(cat)}`)
#         .then(res => res.json())
#         .then(data => {
#           setTopics(prev => ({ ...prev, [cat]: data.topics }));
#         });
#     });
#   }, []);

#   // Function to trigger content pipeline (call your API endpoints)
#   const handleGenerateContent = (category) => {
#     fetch(`/api/generate/${category}`, { method: "POST" })
#       .then(res => res.json())
#       .then(data => {
#         alert(`Content generation started for ${category}`);
#         // Optionally update status
#       });
#   };

#   return (
#     <div style={{ padding: '20px' }}>
#       <h1>Content Creator Studio</h1>
#       {categories.map(cat => (
#         <div key={cat} style={{ marginBottom: '20px' }}>
#           <h2>{cat}</h2>
#           <button onClick={() => handleGenerateContent(cat)}>Generate Content</button>
#           <ul>
#             {topics[cat]?.map((topic, i) => (
#               <li key={i}>{topic}</li>
#             ))}
#           </ul>
#         </div>
#       ))}
#     </div>
#   );
# }

# export default App;