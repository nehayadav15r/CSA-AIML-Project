<!DOCTYPE html>
<html lang="en">
<body>

<h1>🚀 AI Pathfinding Visualizer</h1>

<div class="section">
<h2>📌 Project Overview</h2>
<p>
The AI Pathfinding Visualizer is an interactive simulation tool designed to demonstrate how different pathfinding algorithms work in real time. 
It allows users to visually understand how algorithms explore nodes and determine the shortest path between two points in a grid.
</p>
<ul>
<li>🧠 Helps understand algorithm behavior visually</li>
<li>🎮 Interactive grid-based simulation</li>
<li>⚡ Real-time execution of search algorithms</li>
</ul>
</div>

<div class="section">
<h2>⚙️ Technologies Used</h2>
<table>
<tr>
<th>Component</th>
<th>Technology</th>
</tr>
<tr>
<td>Programming Language</td>
<td>Python 3.x</td>
</tr>
<tr>
<td>Graphics Library</td>
<td>Pygame</td>
</tr>
<tr>
<td>Data Structures</td>
<td>Queue, Stack, Priority Queue</td>
</tr>
<tr>
<td>Algorithms</td>
<td>BFS, DFS, A*</td>
</tr>
</table>
</div>

<div class="section">
<h2>🧩 Core Components</h2>
<ul>
<li>📦 <b>Node Class:</b> Represents each grid cell with properties like position, color, and neighbors</li>
<li>🟦 <b>Grid System:</b> 25x25 structured layout of nodes</li>
<li>🎨 <b>Visualization:</b> Color-coded states for better understanding</li>
</ul>

<table>
<tr>
<th>Color</th>
<th>Meaning</th>
</tr>
<tr>
<td>🟩 Green</td>
<td>Start Node</td>
</tr>
<tr>
<td>🟥 Red</td>
<td>End Node</td>
</tr>
<tr>
<td>⬛ Black</td>
<td>Wall/Obstacle</td>
</tr>
<tr>
<td>🟧 Orange</td>
<td>Visited Node</td>
</tr>
<tr>
<td>🟦 Blue</td>
<td>Final Path</td>
</tr>
</table>
</div>

<div class="section">
<h2>🧠 Algorithms Implemented</h2>

<table>
<tr>
<th>Algorithm</th>
<th>Type</th>
<th>Behavior</th>
<th>Guarantee</th>
</tr>

<tr>
<td>🔵 BFS</td>
<td>Uninformed</td>
<td>Explores level-by-level</td>
<td>Shortest path (unweighted)</td>
</tr>

<tr>
<td>🟣 DFS</td>
<td>Uninformed</td>
<td>Explores deep first</td>
<td>No guarantee</td>
</tr>

<tr>
<td>🟢 A*</td>
<td>Informed</td>
<td>Uses heuristic (Manhattan distance)</td>
<td>Optimal + Efficient</td>
</tr>
</table>

</div>

<div class="section">
<h2>🎮 User Controls</h2>

<table>
<tr>
<th>Action</th>
<th>Control</th>
</tr>

<tr>
<td>Set Start Node</td>
<td>Left Click (1st click)</td>
</tr>

<tr>
<td>Set End Node</td>
<td>Left Click (2nd click)</td>
</tr>

<tr>
<td>Create Walls</td>
<td>Left Click (after)</td>
</tr>

<tr>
<td>Reset Node</td>
<td>Right Click</td>
</tr>

<tr>
<td>Run BFS</td>
<td>Press B</td>
</tr>

<tr>
<td>Run DFS</td>
<td>Press D</td>
</tr>

<tr>
<td>Run A*</td>
<td>Press A</td>
</tr>

<tr>
<td>Reset Grid</td>
<td>Press R</td>
</tr>

</table>

</div>

<div class="section">
<h2>🌍 Project Scope</h2>
<ul>
<li>📚 Educational tool for learning AI algorithms</li>
<li>🎓 Useful for students studying Data Structures & AI</li>
<li>🎮 Can be extended into game development logic</li>
<li>🧭 Applicable in navigation systems and robotics</li>
<li>🚗 Can simulate real-world routing problems</li>
</ul>
</div>

<div class="section">
<h2>🚀 Advantages of This Model</h2>

<table>
<tr>
<th>Feature</th>
<th>Advantage</th>
</tr>

<tr>
<td>Visualization</td>
<td>Improves conceptual clarity</td>
</tr>

<tr>
<td>Interactive UI</td>
<td>Hands-on learning experience</td>
</tr>

<tr>
<td>Multiple Algorithms</td>
<td>Easy comparison</td>
</tr>

<tr>
<td>Real-Time Execution</td>
<td>Better understanding of performance</td>
</tr>

<tr>
<td>Modular Design</td>
<td>Easy to extend and modify</td>
</tr>

</table>

</div>

<div class="section">
<h2>🔮 Future Improvements</h2>

<ul>
<li>➕ Add Dijkstra’s Algorithm</li>
<li>↗️ Enable diagonal movement</li>
<li>🌊 Add weighted nodes (water, mud)</li>
<li>📊 Show real-time stats (nodes explored, time)</li>
<li>🖥️ Improve UI with sidebar controls</li>
<li>🎨 Add themes and animations</li>
<li>🌐 Convert into web-based version</li>
</ul>

</div>

<div class="section">
<h2>📌 Conclusion</h2>
<p>
The AI Pathfinding Visualizer successfully demonstrates how different algorithms behave under the same conditions. 
It highlights the efficiency of A* compared to BFS and DFS by reducing unnecessary exploration using heuristics.
</p>

<p>
This project serves as a strong foundation for understanding real-world applications such as navigation systems, robotics, and AI-driven game development. 
With further enhancements, it can evolve into a powerful educational and practical tool.
</p>

</div>

<div class="section">
<h2>🔗 References</h2>

<ul>
<li>📄 https://www.pygame.org/docs/</li>
<li>📄 https://www.redblobgames.com/pathfinding/a-star/introduction.html</li>
<li>📄 https://docs.python.org/3/library/heapq.html</li>
</ul>

</div>

</body>
</html>
