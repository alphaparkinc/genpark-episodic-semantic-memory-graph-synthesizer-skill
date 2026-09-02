from client import EpisodicSemanticMemoryGraphSynthesizerClient

def main():
    client = EpisodicSemanticMemoryGraphSynthesizerClient()
    res = client.update_user_memory_graph('usr_alex_8812', 'I moved to Tokyo last week')
    print('Episodic Semantic Memory Graph: ' + res['memory_update_id'])
    print('Extracted Facts: ' + str(len(res['extracted_facts'])) + ' facts | Graph Nodes: ' + str(res['memory_graph_nodes_count']))
    print('Knowledge Graph URL: ' + res['user_knowledge_graph_url'])

if __name__ == '__main__':
    main()
