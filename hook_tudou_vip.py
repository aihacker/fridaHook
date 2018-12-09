import sys
import frida


def on_message(message, data):
    type = message["type"]
    msg = message
    if type == "send":
        msg = "[*] {0}".format(message['payload'])
    elif type == 'error':
        msg = message['stack']
    else:
        msg = message
    print(msg)

def hookVip():
    jscode = """
    Java.perform(function () {
        var clazz = Java.use('com.tudou.gondar.request.util.RequestUtils');
        // Whenever button is clicked
        clazz.isVid.overload("java.lang.String").implementation = function () {
            //console.log('test.a has been callled--------------------------------------');

            Java.perform(function () {
                var throwable = Java.use("java.lang.Throwable").$new();
                console.log(throwable.getStackTrace());
            });
            console.log(arguments[0]);
            var tmp=this.isVid(arguments[0]);
            console.log('isVip:'+tmp)
            //console.log('Done hooked--------------------------------------------');
            return true;
        };
    });
    """
    device = frida.get_usb_device()
    # process=device.attach("com.netease.lijun1.myapplication")
    process = frida.get_usb_device().attach("com.tudou.android")
    script = process.create_script(jscode)
    script.on('message', on_message)
    print('[*] Running karaoke')
    script.load()
    sys.stdin.read()

hookVip()