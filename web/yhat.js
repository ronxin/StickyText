jQuery(document).ready(function() {
  var ssel = $('#sample-sel');
  ssel.text('Sample Text: ');
  for (var i = 1; i <= 10; i++) {
    ssel.append('<a id="sample-' + i + '" href="samples/' + i + '.txt">' + i + '</a>&nbsp&nbsp');
    $('#sample-' + i).click(function(e){
      e.preventDefault();
      $.ajax({
        url : $(this).attr("href"),
        success : function(result){
            $("#mytext").val(result);
        }
      });
    })
  }
});