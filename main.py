vertices    = []
normals     = []
indices     = []
uvs         = []

total_vertices = []

with open('barrier.obj', 'r+') as file:

    write = open('result.txt', 'w+')

    content = file.readlines()
    for line in content:

        if line.startswith('v '):
            w = line.split(' ')
            vertices.append([w[1], w[2], w[3]])

        if line.startswith('vn'):
            w = line.split(' ')
            normals.append([w[1], w[2], w[3]])

        if line.startswith('vt'):
            w = line.split(' ')
            uvs.append([w[1], w[2]])

        if line.startswith('f'):
            w = line.split(' ')
            f = [w[1], w[2], w[3]]

            for face in f:
                face_description = face.split('/')
                face_vertex = int(face_description[0]) - 1
                face_normal = int(face_description[1]) - 1
                face_uv     = int(face_description[2]) - 1

                vertex = vertices[face_vertex]
                normal = normals[face_normal]
                uv     = uvs[face_uv]
                complete_vertex = f'{float(vertex[0])}f, {float(vertex[1])}f, {float(vertex[2])}f, {float(normal[0])}, {float(normal[1])}, {float(normal[2])}, {float(uv[0])}, {float(uv[1])},\n'
                write.write(complete_vertex)

