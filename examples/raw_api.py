# coding=utf-8

from libglfw import *

if __name__ == '__main__':
    @GLFWkeyfun
    def InputKey(window, key, scancode, action, mods):
        print(window, key, scancode, action, mods)

    def show_error(code, message):
        print(code, message)

    def _utf(obj):
        if bytes is str:
            return obj
        else:
            return obj.encode()

    def _str(obj):
        if bytes is str:
            return obj
        else:
            return obj.decode()

    ShowError = GLFWerrorfun(show_error)
    glfwSetErrorCallback(ShowError)

    if not glfwInit():
        raise RuntimeError()

    print(glfwGetVersionString().decode())

    bestmode = 0, 0, None

    monitors = glfwGetMonitors()
    for monitor in monitors:
        vidmodes = glfwGetVideoModes(monitor)
        for vidmode in vidmodes:
            if (vidmode.height * vidmode.width) > bestmode[0] * bestmode[1]:
                bestmode = vidmode.width, vidmode.height, monitor


    glfwSetGamma(monitors[0], -1.0)
    gammar = glfwGetGammaRamp(monitors[0])
    glfwSetGammaRamp(monitors[0], gammar)

    window = glfwCreateWindow(800, 600, _utf("Привет, Мир!"), None, None)
    #window = glfwCreateWindow(bestmode[0], bestmode[1], "Привет, Мир!", monitor, None)
    if not window:
        glfwTerminate()
        raise SystemExit()

    glfwMakeContextCurrent(window)

    glfwSetClipboardString(window, _utf("Тест"))
    print(_str(glfwGetClipboardString(window)))

    glfwSwapInterval(1)

    size = glfwGetFramebufferSize(window)
    glfwSetWindowUserPointer(window, size)
    fps, was = 0, glfwGetTime()

    glfwSetKeyCallback(window, InputKey)

    while not glfwWindowShouldClose(window):
        glfwSwapBuffers(window)

        fps, now = fps + 1, glfwGetTime()
        if now - was >= 1.0:
            # print (fps)
            fps, was = 0, now

        glfwPollEvents()

        if glfwGetKey(window, GLFW_KEY_ESCAPE):
            glfwSetWindowShouldClose(window, True)

    try:
        print (glfwGetWindowUserPointer(window))
    except:
        print ('Set/Get UserPointer is not supported')

    glfwDestroyWindow(window)

    glfwTerminate()
