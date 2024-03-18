import OpenGL.GL as gl
from OpenGL.GL import shaders


class lazy_class_attribute(object):
    def __init__(self, function):
        self.fget = function

    def __get__(self, obj, cls):
        value = self.fget(obj or cls)
        # note: 인스턴스가 아닌 클래스 객체에 저장한다.
        #       클래스-레벨 또는 인스턴스-레벨 접근과 관계없다.
        setattr(cls, self.fget.__name__, value)
        return value


class ObjectUsingShaderProgram(object):
    # 전형적인 pass-through vertex shader 구현
    VERTEX_CODE = """ 
        #version 330 core 
        layout(location = 0) in vec4 vertexPosition; 
        void main(){ 
            gl_Position =  vertexPosition; 
        } 
    """
    # 전형적인 프래그먼트 셰이더 
    # 모든 요소를 흰색으로 그린다.
    FRAGMENT_CODE = """ 
        #version 330 core 
        out lowp vec4 out_color; 
        void main(){ 
            out_color = vec4(1, 1, 1, 1); 
        } 
    """

    @lazy_class_attribute
    def shader_program(self):
        print("compiling!")
        return shaders.compileProgram(
            shaders.compileShader(self.VERTEX_CODE, gl.GL_VERTEX_SHADER),
            shaders.compileShader(self.FRAGMENT_CODE, gl.GL_FRAGMENT_SHADER),
        )
