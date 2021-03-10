$(function() {
    var count = 0;
    $('tr.row-1 div').click(function(status){
        clicked_column_class = 'tr td.col-' + $('tr.row-1 div').index(this);

        tr_num = $('tr').length;
        console.log(clicked_column_class);

        element_to_change = 2;

        if (count % 2) {
            status = false;
            class_name = 'red-oval';
        } else {
            status = true;
            class_name = 'blue-oval';
        }

         count += 1;


         console.log(count);
        $(clicked_column_class + ' div.grey-oval').eq(-1).removeClass('grey-oval').addClass(class_name);
        console.log(status);
    });
});