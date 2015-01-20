var Sorter = ( function($) {
        
        var setListeners = function() {
            var rating = $('#rating-button').on('click', function() {
                sortByCol(1);
            });
        }

        var sortByCol = function(colId) {
            var table = document.getElementById('table-body');
            var arr = [];
            
            console.log(table); 
            for (var i = 0; i < table.rows.length; i++) {
                cells = table.rows[i].cells
                arr[i] = []
                for (var j = 0; j < cells.length; j++) {
                    arr[i][j] = cells[j].innerHTML;
                }
            }

            arr.sort(function(a, b) {
                return (b[colId] - a[colId]);
            });

            for (var i = 0; i < table.rows.length; i++) {
                arr[i] = "<td>" + arr[i].join("</td><td>") + "</td>";
            }
            table.innerHTML = "<tr>" + arr.join("</tr><tr>") + "</tr>";
        }

        return {
            init: setListeners
        }

})(jQuery);

$(window).on('load', function() {
    Sorter.init()
})
