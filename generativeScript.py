import bpy
import random
from pprint import pprint

class Gemesis:
    def __init__(self, gemId, upperBox, lowerBox, background, crystal):
        #randomly asign different properties to gem
        self.gemId = gemId
        self.upperBox = upperBox
        self.lowerBox = lowerBox
        self.background = background
        self.crystal = crystal
        #kirstalColor = null;
        
    def hashMe(self):
        #do hash
        print("hashing")
        
class Traits:
    def __init__(self):
        #ADD ALL OBJECTS FROM ONE COLLECTION TO EACH LIST
        self.upperBoxes = bpy.data.collections['UpperBoxes'].all_objects  #objects in objects are not good as they get displayed seperately
        self.lowerBoxes = bpy.data.collections['LowerBoxes'].all_objects
        self.crystals = bpy.data.collections['Crystals'].all_objects
        self.backgrounds = bpy.data.collections['Backgrounds'].all_objects
        
        #ADD ALL MATERIAL TO EACH LIST
        self.upperBoxesMaterials = bpy.data.materials
      
        
class GemesisGenerator():
    
    def createRandomGem(gemId, traits):
        #RANDOMLY CHOOSE ONE OF THE TRAITS (OBJECTS)
        upperBox = random.choice(traits.upperBoxes)
        lowerBox = random.choice(traits.lowerBoxes)
        background = random.choice(traits.backgrounds)
        crystal = random.choice(traits.crystals)
        
        #CREATE GEM WITH CHOSEN TRAITS
        gemesis = Gemesis(gemId, upperBox, lowerBox, background, crystal) 
        
        #MAKE ONLY CHOSEN ITEMS VISIBLE AND RENDERABLE
        bpy.data.objects[gemesis.upperBox.name].hide_render = False
        bpy.data.objects[gemesis.upperBox.name].hide_viewport = False
        bpy.data.objects[gemesis.upperBox.name].hide_set(False)
        
        bpy.data.objects[gemesis.lowerBox.name].hide_render = False
        bpy.data.objects[gemesis.lowerBox.name].hide_viewport = False
        bpy.data.objects[gemesis.lowerBox.name].hide_set(False)
        
        bpy.data.objects[gemesis.background.name].hide_render = False
        bpy.data.objects[gemesis.background.name].hide_viewport = False
        bpy.data.objects[gemesis.background.name].hide_set(False)
        
        bpy.data.objects[gemesis.crystal.name].hide_render = False
        bpy.data.objects[gemesis.crystal.name].hide_viewport = False
        bpy.data.objects[gemesis.crystal.name].hide_set(False)
        
        
        print("Gem with gemId " + str(gemId) + " created")


    def hideAll():
        bpy.ops.object.select_all(action='DESELECT')
        #Unhide all inactive objects
        for obj in bpy.data.objects:
            #obj.hide_viewport = False #Enable visibility in all viewports
            obj.hide_render = True #Enable the object in renders
            obj.hide_set(True) #Enable the object in the viewport
            obj.hide_select = True #Enable selection in the viewport

    def showLights():
        #for light in bpy.data.collections['Lights'].all_objects:
            #obj.hide_viewport = False #Enable visibility in all viewports
            #light.hide_render = False #Enable the object in renders
            #light.hide_set(False) #Enable the object in the viewport
            #light.hide_select = False #Enable selection in the viewport
        print("ShowLights")

    def unHideAll():
        bpy.ops.object.select_all(action='DESELECT')
        #Unhide all inactive objects
        for obj in bpy.data.objects:
            obj.hide_render = False #Enable the object in renders
            obj.hide_set(False) #Enable the object in the viewport
            obj.hide_select = False #Enable selection in the viewport
        print("Unhidden")
    
    def safeGemInFile():
        #safe the gem in file
        donothing = 0
    
    
    ##DO THE MAIN STUFF
    i = 1;          #gemID
    maxAmount = 2   #amount of gems you want to create
    while i <= maxAmount:
        hideAll()
        traits = Traits()
        createRandomGem(i, traits)
        
        #for obj in bpy.data.objects:
            #pprint(obj)
        #print("______________________________________________")
        #for light in bpy.data.collections['Lights'].all_objects:
            #pprint(light)
        
        i = i + 1
        
        
#INFO        
  #PRINTS ALL Properties OF OBJECT
        #pprint(vars(my_object))
   