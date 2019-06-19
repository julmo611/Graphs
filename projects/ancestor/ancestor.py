def earliest_ancestor(data, id, ancestor=None):
    if ancestor == None:
        ancestor = [[id]]

    for i in range(len(data)):
        if data[i][1] == id:

            bloodline = [list(ancestor[j])
                         for j in range(len(ancestor)) if ancestor[j][-1] == id][0]
            bloodline.append(data[i][0])

            ancestor.insert(0, bloodline) if len(bloodline) > len(
                ancestor[0]) else ancestor.append(bloodline)

            earliest_ancestor(data, data[i][0], ancestor)
    return min([x[-1] for x in ancestor if len(x) == len(ancestor[0])]) if len(ancestor) > 1 else -1
