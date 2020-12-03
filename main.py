from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivymd.uix.textfield import MDTextField,MDTextFieldRect
import os
import subprocess
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.tooltip import MDTooltip
from kivymd.uix.button import MDRectangleFlatButton,MDRoundFlatButton,MDFillRoundFlatButton,MDIconButton
script='''
ScreenManager:
    Main:
    Release
    Operate:
    SpecsEdit:
    ApkInfo:
    SignInfo:

<Main>:
    name:'main'


    MDTextField:
        id:proj
        hint_text:'name of project folder name only..'
        pos_hint:{'center_x':0.23,'center_y':0.9}
        size_hint_x:0.42
        mode: "rectangle"
    
    Label:
        text:'[color=#ff0015][b]Note[/b][/color]:Read instrcutions first to avoid errors'
        color:0,0,0,1
        pos_hint:{'center_x':0.73,'center_y':0.9}
        markup:True
  

    Label:
        text:'[color=#ff0015][b]Note[/b][/color]:use your script name only as main.py,for avoid errors'
        color:0,0,0,1
        pos_hint:{'center_x':0.4,'center_y':0.8}
        markup:True

    Label:
        text:'[color=#ff0015][b]Note[/b][/color]:Before starting plase enable virtual env. in terminal'
        color:0,0,0,1
        pos_hint:{'center_x':0.4,'center_y':0.75}
        markup:True


    MDRectangleFlatButton:
        text:'Read Instrcution'
        pos_hint:{'center_x':0.88,'center_y':0.78}
        size_hint_x:0.2
        on_release:
            root.manager.transition.direction='down'
            root.manager.transition.duration= 0.3
            root.manager.current='operate'

    Label:
        text:'------------------------------------------------------------------------'
        pos_hint:{'center_x':0.5,'center_y':0.7}
        color:0,0,0,1

    Label:
        text:'[b]Step 1: Making buildozer.specs[/b]'
        pos_hint:{'center_x':0.25,'center_y':0.65}
        markup:True
        color:0,0,0,1


    MDFillRoundFlatButton:
        text:'Make [b]buildozer.spec[/b] file in path.'
        pos_hint:{'center_x':0.7,'center_y':0.65}
        markup:True
        on_release:
            root.build_specs()
            root.dispaly_war()


    Label:
        text:'[b]Step 2: Edit buildozer.spec file[/b]'
        pos_hint:{'center_x':0.25,'center_y':0.55}
        markup:True
        color:0,0,0,1


    MDRoundFlatButton:
        text:'Read Instrcutions.'
        pos_hint:{'center_x':0.7,'center_y':0.55}
        on_release:
            root.manager.transition.direction='up'
            root.manager.transition.duration= 0.3
            root.manager.current='specedit'
            
    Label:
        text:'[b]Step 3: Making apk.[/b]'
        color:0,0,0,1
        pos_hint:{'center_x':0.17,'center_y':0.45}
        markup:True

    MDRoundFlatButton:
        text:'Read Instrcutions.'
        pos_hint:{'center_x':0.7,'center_y':0.45}
        on_release:
            root.manager.transition.direction='up'
            root.manager.transition.duration= 0.3
            root.manager.current='apkinfo'

    Label:
        text:'-------------------------------------------------------------------------'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        color:0,0,0,1  

    MDFillRoundFlatButton:
        text:'Making Debug apk.'
        pos_hint:{'center_x':0.2,'center_y':0.3}
        on_release:
            root.debug_apk()

   
    MDFillRoundFlatButton:
        text:'Making Release apk.'
        pos_hint:{'center_x':0.5,'center_y':0.3}
        on_release:
            root.release_apk()


    Label:
        text:"[b]After making Release apk don't forget to signing it. It is necessary part.[/b]"
        color:0,0,0,1
        pos_hint:{'center_x':0.5,'center_y':0.19}
        markup:True

    Label:
        text:'-------------------------------------------------------------------------'
        pos_hint:{'center_x':0.5,'center_y':0.15}
        color:0,0,0,1  


    MDFillRoundFlatButton:
        text:'Signing release apk.'
        pos_hint:{'center_x':0.5,'center_y':0.07}
        on_release:
            root.manager.transition.direction='up'
            root.manager.transition.duration= 0.3
            root.manager.current='release'
           



<Release>:
    name:'release'
    MDTextField:
        id:folder
        hint_text:'Enter keystore folder name'
        pos_hint:{'center_x':0.24,'center_y':0.9}
        size_hint_x:0.40
        mode: "rectangle"
        
    MDTextField:
        id:key
        hint_text:'Enter your-key-name name'
        pos_hint:{'center_x':0.75,'center_y':0.9}
        size_hint_x:0.40
        mode: "rectangle"
    
    MDTextField:
        id:password
        hint_text:'Enter key password atleast 8'
        pos_hint:{'center_x':0.24,'center_y':0.78}
        size_hint_x:0.40
        mode: "rectangle"
        
    MDTextField:
        id:dname
        hint_text:'Enter devloper name'
        pos_hint:{'center_x':0.75,'center_y':0.78}
        size_hint_x:0.40
        mode: "rectangle"
        
    MDTextField:
        id:ouname
        hint_text:'Organisation-unit-name name'
        pos_hint:{'center_x':0.24,'center_y':0.66}
        size_hint_x:0.40
        mode: "rectangle" 
        
    MDTextField:
        id:oname
        hint_text:'Enter organisation-name'
        pos_hint:{'center_x':0.75,'center_y':0.66}
        size_hint_x:0.40
        mode: "rectangle"  
        
    MDTextField:
        id:city
        hint_text:'Enter city/locality name'
        pos_hint:{'center_x':0.24,'center_y':0.54}
        size_hint_x:0.40
        mode: "rectangle" 
        
    MDTextField:
        id:state
        hint_text:'Enter state/provicences name'
        pos_hint:{'center_x':0.75,'center_y':0.54}
        size_hint_x:0.40
        mode: "rectangle" 
    
    MDTextField:
        id:ccode
        hint_text:'Enter 2-letter country-code.'
        pos_hint:{'center_x':0.24,'center_y':0.42}
        size_hint_x:0.40
        mode: "rectangle" 
    
    
    MDIconButton:
        icon: "language-python"
        pos_hint: {"center_x":0.5, "center_y": 0.42}
        on_release:
            root.info()
    
 
    
    MDTextField:
        id:unapk
        hint_text:'Enter name of unsigned apk'
        pos_hint:{'center_x':0.24,'center_y':0.30}
        size_hint_x:0.40
        mode: "rectangle" 
    
    MDTextField:
        id:fapk
        hint_text:'name of final apk without.apk ex.'
        pos_hint:{'center_x':0.75,'center_y':0.30}
        size_hint_x:0.40
        mode: "rectangle" 
       

    
    MDFillRoundFlatButton:
        text:'Sign apk.'
        pos_hint:{'center_x':0.25,'center_y':0.12}
        on_release:
            root.sign_apk()
            root.manager.transition.direction='down'
            root.manager.transition.duration= 0.3
            root.manager.current='signinfo'
            

    MDFillRoundFlatButton:
        text:'Genreating key'
        pos_hint:{'center_x':0.75,'center_y':0.42}
        on_release:
            root.genreate_key()    

    Label:
        text:'[color=#ff0015][b]Note[/b][/color]:Check here its IMP!'
        color:0,0,0,1
        pos_hint:{'center_x':0.75,'center_y':0.18}
        markup:True

    MDRoundFlatButton:
        text:'Read Instrcutions.'
        pos_hint:{'center_x':0.75,'center_y':0.10}

<Operate>:
    name:'operate'
    MDTextFieldRect:
        text:root.textf()
        markup:True
        size_hint:0.95,0.95
        pos_hint:{'center_x':.5,'center_y':.5}
        readonly:True
        
    MDRoundFlatButton:
        text:'Back'
        pos_hint:{'center_x':0.9,'center_y':0.1}
        on_release:
            root.manager.transition.direction='down'
            root.manager.transition.duration= 0.3
            root.manager.current='main'
        
<SpecsEdit>:
    name:'specedit'
    MDTextFieldRect:
        text:root.textf()
        markup:True
        size_hint:0.95,0.95
        pos_hint:{'center_x':.5,'center_y':.5}
        readonly:True
        
    MDRoundFlatButton:
        text:'Back'
        pos_hint:{'center_x':0.9,'center_y':0.1}
        on_release:
            root.manager.transition.direction='down'
            root.manager.transition.duration= 0.3
            root.manager.current='main'

<ApkInfo>:
    name:'apkinfo'
    MDTextFieldRect:
        text:root.textf()
        markup:True
        size_hint:0.95,0.95
        pos_hint:{'center_x':.5,'center_y':.5}
        readonly:True
        
    MDRoundFlatButton:
        text:'Back'
        pos_hint:{'center_x':0.9,'center_y':0.1}
        on_release:
            root.manager.transition.direction='down'
            root.manager.transition.duration= 0.3
            root.manager.current='main'

<SignInfo>:
    name:'signinfo'
    MDTextFieldRect:
        text:root.textf()
        markup:True
        size_hint:0.95,0.95
        pos_hint:{'center_x':.5,'center_y':.5}
        readonly:True
        
    MDRoundFlatButton:
        text:'Back'
        pos_hint:{'center_x':0.9,'center_y':0.1}
        on_release:
            root.manager.transition.direction='down'
            root.manager.transition.duration= 0.3
            root.manager.current='main'
'''


Window.size=(550,450)

class SignInfo(Screen):
    def textf(self):
        text="""
------------------------------------------------------
Please read this this is very IMPORTENT............
______________________________________________________

After click on sign apk button You must have to follow these steps in order to complete Signing apk..
    
    Step1: We make a unaligned apk in your bin directory, please copy it..
    Step2: Now go to your /Home folder manually
    Step3: Now search for .buldozer folder (if not found, try to activate show hidden file options.)
    Step4: Now to android/platform/android-sdk/build-tools/30.0.2 manaully
                                                          ^^^^^^^^
                             This folder varies according to diffrent android-sdk verson
                             
    Step4: From your keystore folder copy .jks file to this directory
    Step5: Now open terminal in the directory and run following code:
    
           $ ./apksigner sign --ks Keyname.jks --out YourFinalApkName.apk YourUnalignedApkName.apk
                                   ^^^^^^^^^^^
                                   your key name
                       
    Step6: This Will creted a final release signed apk for you in current directory.
    
    
    Note in This process This Will ask for password of keystore, it will store for you in your keystore folder as keyinfo.txt.
    
    
    ---------------------------------------------------------------
        """
        return text

class ApkInfo(Screen):
    def textf(self):
        text="""
        
There are two type of apk>
    1>Debug apk
    2>Release apk
    
    Debug Apk:
        this is apk which you created to know the errors in apk when it is run on your mobile phone.
    Release apk:
        simply it is final apk with do not let you know debugging informations.
        
    It is recommended that first you created debug apk to check is your apk works or not.
    
    Information:::::
        After making release apk your must have to sign it, or otherwise it is not work.
        

        """
        return text

class SpecsEdit(Screen):
    def textf(self):
        text="""----------------------------------------------------------------------------------
This contain how to edit buildozer.spec file and Some Warnings.
----------------------------------------------------------------------------

After succesfully creation of buildozer.spec file please edit it carefully.
Open buildozer.spec file and make the following changes:
    
 Line no. --4. title of your app
    -7 your app package name (simple your app name)
    -10 package_domain= e.g, com.example.appname (This will unique, donot let it org.test)
    
    -31 verson of your app, e.g, 0.1 or 1.0
    -39 requirements: the python module you use in main.py (please include cython either you don't use it.)
        e.g, requirements = python3,kivy,wikipedia,kivymd
        
    -46 this inclue the image name you want to show in startup as boot logo.
        e.g, presplash.filename = plash.png (Let it empty and it will show kivy logo)
    
    -49 icon.filename=icon.png (your icon image)
    
    -82 this contain backgroud color of boot startup winodw.
        e.g, android.presplash_color = #000000
    
    -91 all permissons your apk take from android phone.
        e.g, android.permissions = INTERNET,ACCESS_NETWORK_STATE
    
    -97 max. android verson your apk support
        note: api no. is d/f for all android verson, please check them on android devlopment website.
        e.g, android.api = 29
        
    -100 min. android verson your apk will support.
    
    -132 Please edit it to True.
        e.g, android.accept_sdk_license = True
    
    -226 the android architecture your apk support.
        
        if you make apk for disturbution you should make apk for all architecture.
        
        e.g, android.arch = arm64-v8a
        
        """
        return text

class Operate(Screen):
    def textf(self):
        text='''----------------------------------------------------------------------------------
Note:Please read this Carefully if you use this first time:
Instrcution-Make sure you are fully filled with following requirements..
    Note:All given conditions are necessey
    
    
1> A virtual Enviroment.
2> Buldozer pre-installed. (Guide of installtion is given below..)
3> A portable Working directory. (Means you must donot have any file out of main directory)
4> Main python file must be name as main.py only for avoide any errors.
5> A active Internet connections. (Require by buildozer for downloading necessary files.)
6> Some pre installed python library according to your project. (Names will given below.)

_____________________________________________________________

Virtual Enviroment:::::::

    You must have a virtual enviroment in order to run buildozer and this Program.
    Please make sure you activate your virtual enviroment first in terminal and than activate this program.
    
    ~ Guide of activateing Virtual Enviroment:
        
        > In terminal first, change directory to yur virtual env. folder
        > than run this command:
            $ source mykivyinstall/bin/activate
                     ^^^^^^^^^^^^
                     Virtual env folder name
                     
        >Than execute this progeram using:
            $ python main.py
            
  #  ~ Guide of Installing Virtual Enviroment:        
  #      
  #      >First install it via 
  #          $ python3 -m pip install -upgrade pip
  #          $ pip3 install virtualenv
    

_____________________________________________________________

Buldozer:
    ~ Guide of installing buildozer:
        
        > first make sure your activate your virtual env.
        > install buildozer via git (you can install also via pip but it make some errors for me.)
            
            $ git clone https://github.com/kivy/buildozer
            $ cd buildozer 
            $ python setup.py build
            $ pip install -e
            
                note: you can install git via sudo apt-get install git
        
_____________________________________________________________

Some pre-installed python libraries:

    > cython
    > jinus
    >requests (if your app requires a active Internet connections)
    > bs4,beautifulsoup4 (if your app requires a active Internet connections)
    > urllib3 (if your app requires a active Internet connections)
Some installed modules in system:
    
    >lld
        install via:
            $ sudo apt-get install lld
            
        
        '''
        return text


class Main(Screen):
    
    def dispaly_war(self):
        d=MDDialog(title='',text="Please make sure you enable android.accept_sdk_license to true in buildozer.spec file. ",size_hint=(0.5,0.3))
        d.open()        
        

    def build_specs(self):
        project=self.ids.proj
      
    # subprocess.run(['source',str(virtual_fol.text)+'/bin/activate'],stdout=subprocess.PIPE)
        if os.path.isdir(str(project.text))==True:
            pass
        else:
            os.mkdir(str(project.text))        
        os.chdir(str(project.text))

        if os.path.isfile('buildozer.spec')==True:
            pass
        else:
            make=subprocess.run(['buildozer','init'],stdout=subprocess.PIPE)

         

        if os.path.isfile('buildozer.spec')==True:
            di=MDDialog(title='',text='buldozer.specs creted succesfully',size_hint=(0.88,0.5))
            di.open()
            
            spec_file=open('buildozer.spec','r')
            lic=spec_file.readlines()
            spec_file=open('buildozer.spec','w')
            lic[132]='android.accept_sdk_license = True\n'
            spec_file.writelines(lic)
            spec_file.close()

        else:
            open_di=MDDialog(title='',text='buldozer.specs file creation failed\nKindley see log in terminal',size_hint=(0.85,0.5))
            open_di.open()
            
        

    def debug_apk(self):
        project=self.ids.proj
        if str(project.text)=='':
            open_di=MDDialog(title='',text='Please enter project folder name',size_hint=(0.85,0.5))
            open_di.open()
        else:
            p=subprocess.run(['buildozer','-v','android','debug'],stdout=subprocess.PIPE)
            open_di=MDDialog(title='',text='Making debug apk is in process:Please ensure to enable Internet.\nKindly see the terminal..',size_hint=(0.85,0.5))
            open_di.open()    
            print(str(p.stdout.decode('utf-8')))
            
    def release_apk(self):
        project=self.ids.proj       
        if str(project.text)=='':
            open_di=MDDialog(title='',text='Please enter project folder name',size_hint=(0.85,0.5))
            open_di.open()
        else:
            p=subprocess.run(['buildozer','android','release'],stdout=subprocess.PIPE)
            open_di=MDDialog(title='',text='Making release apk is in process:Please ensure to enable Internet.\nKindly see the terminal..',size_hint=(0.85,0.5))
            open_di.open()    
            print(str(p.stdout.decode('utf-8')))
    
        

class Release(Screen):
    def info(self):
        d=MDDialog(title='',text="Country code example:\n 'in' for India (Without quotes)\n'us' for USA.",size_hint=(0.5,0.3))
        d.open()
    
    
    def genreate_key(self):
        keystore=self.ids.folder
        key=self.ids.key
        password=self.ids.password
        devloper=self.ids.dname
        orgu=self.ids.ouname
        org=self.ids.oname
        city=self.ids.city
        state=self.ids.state
        country=self.ids.ccode
        
        
        cmd=['mkdir','-p','./'+str(keystore.text)+'/']
      #  cmd=['mkdir','-p','./keys/']
        subprocess.run(cmd,stdout=subprocess.PIPE)
        ip=str(str(password.text)+'\n'+str(password.text)+'\n'+str(devloper.text)+'\n'+str(orgu.text)+'\n'+str(org.text)+'\n'+str(city.text)+'\n'+str(state.text)+'\n'+str(country.text)+'\nyes\n'+str(password.text)+'\n'+str(password.text)).encode('utf-8')
      #  ip='abc123def456\nabc123def456\nMohit Devli\norgunit\norgname\ncitylocatilt\nstateprovicence\n2lettercountrycode\nyes\nabc123def456\nabc123def456\nabc123def456'.encode('utf-8')
        print('Your all selection are:')
        print(ip)
        c=['keytool','-genkey','-v','-keystore','./'+str(keystore.text)+'/'+str(key.text)+'.jks','-alias',str(key.text),'-keyalg','RSA','-keysize','2048','-validity','10000']
       # c=['keytool','-genkey','-v','-keystore','./keys/your-new-key.keystore','-alias','your-key-alias','-keyalg','RSA','-keysize','2048','-validity','10000']
        k=subprocess.run(c,stdout=subprocess.PIPE,input=ip)
        print(k.stdout.decode('utf-8'))
        
        
        infofile=open('keyinfo'+str(keystore.text)+'.txt','w')
        infofile.writelines('Keystore name:  '+str(keystore.text)+'\nkey_name:  '+str(key.text)+'\nkey_password:  '+str(password.text)+'\nDevloper:  '+str(devloper.text)+'\nOrganistion_unit:  '+str(orgu.text)+'\nOrganistaion name:  '+str(org.text)+'\ncity:  '+str(city.text)+'\nstate:  '+str(state.text)+'\nTwo-Letter Country code:  '+str(country.text))
        
    def sign_apk(self):
        print('\n\n-----------------------------------------------------------------------')
        unsign=self.ids.unapk
        final=self.ids.fapk
        
        cmd=['zipalign','-v','4','./bin/'+str(unsign.text),'./bin/'+str(final.text)+'_unaligned.apk']
        s=subprocess.run(cmd,stdout=subprocess.PIPE)
        print(s.stdout.decode('utf-8'))
        
        
       # zipalign -v 4 ./bin/com.guy-release-unsigned.apk ./bin/myapp-aligned.apk
        
        
        
sm=ScreenManager()
sm.add_widget(Main(name='main'))
sm.add_widget(Release(name='release'))
sm.add_widget(Operate(name='operate'))
sm.add_widget(SpecsEdit(name='specedit'))
sm.add_widget(ApkInfo(name='apkinfo'))
sm.add_widget(SignInfo(name='signinfo'))

class pyAutoBuildApksApp(MDApp):
    def build(self):
        kv=Builder.load_string(script)
        return kv

pyAutoBuildApksApp().run()
