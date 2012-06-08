var color = d3.scale.category20();
var w = 1200, h = 800;
var s = $('#teams');
var selected_team = teams[0];

$(function(){
    for (idx in teams) {
        s.append($('<option id="t'+idx+'">'+teams[idx]+'</option>'));
    }
    s.change(function(evt){
        selected_team = $(this).val();
        showGraph(graphs[selected_team]);
    });
    showGraph(graphs[selected_team]);
});

function showGraph(graph) {
    $('#vis').empty();
    var vis = d3.select('#vis').append('svg:svg')
        .attr('width', w)
        .attr('height', h);

    var force = null;
    force = self.force = d3.layout.force()
        .nodes(graph.nodes)
        .links(graph.links)
        .gravity(.04)
        .distance(120)
        .charge(-150)
        .size([w, h])
        .start();

    var link = vis.selectAll('line.link')
        .data(graph.links)
        .enter().append('svg:line')
        .attr('class', 'link')
        .attr('x1', function(d) { return d.source.x; })
        .attr('y1', function(d) { return d.source.y; })
        .attr('x2', function(d) { return d.target.x; })
        .attr('y2', function(d) { return d.target.y; });

    var node = vis.selectAll('g.node')
        .data(graph.nodes)
      .enter().append('svg:g')
        .attr('class', 'node')
        .call(force.drag);

    node.append('circle')
        .attr('class', 'node')
        .attr('r', 7)
        .style('fill', function(d) { return color(d.group); });

    node.append('svg:text')
        .attr('class', function(d) { return (selected_team === d.team) ? 'nodetext current' : 'nodetext'; })
        .attr('dx', 12)
        .attr('dy', '.35em')
        .text(function(d) { return d.name; });

    force.on('tick', function() {
      link.attr('x1', function(d) { return d.source.x; })
          .attr('y1', function(d) { return d.source.y; })
          .attr('x2', function(d) { return d.target.x; })
          .attr('y2', function(d) { return d.target.y; });

      node.attr('transform', function(d) { return 'translate(' + d.x + ',' + d.y + ')'; });
    });
}
