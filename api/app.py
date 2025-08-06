from flask import Flask, jsonify
from api.scrapers import topic_fetcher

app = Flask(__name__)

@app.route('/api/topics/<category>')
def get_topics(category):
    topics = topic_fetcher.fetch_topics(category)
    return jsonify({"category": category, "topics": topics})

if __name__ == '__main__':
    app.run(debug=True, port=5000)


# npx create-react-app content-dashboard
# cd content-dashboard


# // dashboard/src/App.js
# import React, { useState, useEffect } from 'react';

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

#   useEffect(() => {
#     categories.forEach(cat => {
#       fetch(`http://localhost:5000/api/topics/${encodeURIComponent(cat)}`)
#         .then(res => res.json())
#         .then(data => {
#           setTopics(prev => ({ ...prev, [cat]: data.topics }));
#         });
#     });
#   }, []);

#   return (
#     <div>
#       <h1>Content Creator Studio Dashboard</h1>
#       {categories.map(cat => (
#         <div key={cat}>
#           <h2>{cat}</h2>
#           <ul>
#             {topics[cat]?.map((topic, i) => <li key={i}>{topic}</li>)}
#           </ul>
#         </div>
#       ))}
#     </div>
#   );
# }

# export default App;