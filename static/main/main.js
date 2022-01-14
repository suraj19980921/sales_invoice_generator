
        var count = 0;
        
    
        $('#add_more').click(function(event){

           count = count + 1;
            
            console.log(count);

            const clone = $("#product_0").clone();
            clone.attr('id', 'product_'+count);

            clone.find("[name='product_name_0']").attr({id:'product_name_'+count , name:'product_name_'+count});
            clone.find("[name='quantity_0']").attr({id:'quantity_'+count , name:'quantity_'+count});
            clone.find("[name='amount_0']").attr({id:'amount_'+count , name:'amount_'+count});
            clone.find("[id='remove_0']").attr({id:'remove_'+count ,style:'display : block'});
            

            clone.find("[name='product_name_"+count+"']").val('')
            clone.find("[name='quantity_"+count+"']").val('')
            clone.find("[name='amount_"+count+"']").val('')

            clone.appendTo('#product_purchased'); 

            $("#forms_count").val(count+1);


        });

       function remove(identity){
          console.log(identity);
           var product = $("#"+identity+"").parent().parent().attr('id');
            $("#"+product+"").remove();
            
       }