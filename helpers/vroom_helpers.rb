module VroomHelpers

   def vroom_example_image(modname, function, filename)
      relpath = "examples/#{modname}/#{function}/#{filename}"
      if File.exists?("./source/assets/img/#{relpath}")
         "<img src='/assets/img/#{relpath}' width='400' height='225'/>"
      else
         '<img src="holder.js/400x225/social"/>'
      end
   end

end
