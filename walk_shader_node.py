import bpy

def walk_group(group, func, output_type=bpy.types.ShaderNodeOutputMaterial):
    outputs = [n for n in group.nodes if isinstance(n, output_type)]
    for output in outputs:
        walk_node(output, func)
    
def walk_node(node, func):
    func(node)
    inputs = node.inputs
    for i_socket in inputs:
        for link in i_socket.links:
            next_node = link.from_node
            if isinstance(next_node, bpy.types.ShaderNodeGroup):
                walk_group(next_node.node_tree, func, bpy.types.NodeGroupOutput)
            walk_node(next_node, func)
