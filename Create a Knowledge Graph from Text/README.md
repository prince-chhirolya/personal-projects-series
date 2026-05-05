# Create a Knowledge Graph from Text

## Technologies Used
<p style='font-weight: bold'>
spaCy | Python | NetworkX | Matplotlib | NLP
</p>

## Project Description
A knowledge graph is widely used to concentrate knowledge in a compact and cohesive form for easy retrieval. Creating a knowledge graph involves getting data, preprocessing it, converting words to their root forms, and extracting subject-predicate-object triple.

In this project, we’ll use The Wikipedia Library to get English language sentences and pass them through every step listed above to create a knowledge graph at the end. The graph will also facilitate information extraction via simple queries. All the text processing will be done via the open-source NLP library, spaCy. The network creation and information extraction will be completed using the NetworkX library, and lastly, the pyvis library will be used to display the knowledge graph.