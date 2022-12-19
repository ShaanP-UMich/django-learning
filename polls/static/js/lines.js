new LeaderLine(
    document.getElementById('start'),
    document.getElementById('end')
)

new LeaderLine(
    document.getElementById('node1'),
    document.getElementById('node2')
).setOptions({path: 'arc'})

new LeaderLine(
    document.getElementById('node1'),
    document.getElementById('node4')
).setOptions({path: 'arc'})

new LeaderLine(
    document.getElementById('node2'),
    document.getElementById('node8')
).setOptions({path: 'arc'})