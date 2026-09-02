class EpisodicSemanticMemoryGraphSynthesizerClient:
    def update_user_memory_graph(self, user_id='usr_991823', new_interaction_text='User prefers dark mode and is building an e-commerce platform using Next.js and Tailwind.'):
        return {
            'memory_update_id': 'mem_upd_9918',
            'user_id': user_id,
            'extracted_facts': [
                {'entity': 'User', 'relation': 'PREFERS', 'target': 'Dark Mode'},
                {'entity': 'User', 'relation': 'BUILDING', 'target': 'E-Commerce Platform (Next.js/Tailwind)'}
            ],
            'memory_graph_nodes_count': 12,
            'contradiction_resolved': False,
            'user_knowledge_graph_url': 'https://memory.graph.genpark.ai/users/9918.json'
        }
