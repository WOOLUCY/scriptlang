#include <Python.h>
#include <string.h>

static PyObject* cLink_strlen(PyObject* self, PyObject* args) {
	char* str;

	if (!PyArg_ParseTuple(args, "s", &str))
		return NULL;

    int size = 0;
    for (int i = 0;; i++)
    {
        if (str[i] & 0x80)     // 한글이다! 배열 인식의 키인 i를 1번더 증가시키자!
        {
            size++;
            i += 2;
        }

        else if (str[i] == '\0')  // 문자열의 끝이다! '' 이다! 종료~
            break;

        else                    // 아니면 일반 아스키로 간주하고 사이즈 1 증가!
            size++;
    }
    
	return Py_BuildValue("i", size - 1);
}

// 3. 모듈에 등록할 함수 정의를 담은 배열(__dict__ 속성이 됨) 
static PyMethodDef CLinkMethods[] = {
	{"strlen", cLink_strlen, METH_VARARGS, "count a string length."},
	{NULL, NULL, 0, NULL} // <- 배열 끝 표시. 
};

static PyModuleDef cLinkmodule = { //2. 생성할 모듈 정보를 담는 구조체
	PyModuleDef_HEAD_INIT,
	"cLink",
	"It is a test module.",
	-1, CLinkMethods //3. CLinkMethods 배열 참조
};

//1. 파이썬 인터프리터에서 import할 때 실행 (PyInit_<module> 함수)
PyMODINIT_FUNC PyInit_cLink(void) {
	return PyModule_Create(&cLinkmodule); //2. cLinkmodule 구조체 참조
}