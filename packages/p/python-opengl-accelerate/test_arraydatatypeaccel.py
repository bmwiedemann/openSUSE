import unittest, ctypes
from OpenGL.arrays import arraydatatype as adt
from OpenGL.arrays import vbo
from OpenGL import GL
from OpenGL._bytes import integer_types
try:
    import numpy 
except ImportError:
    numpy = None

class _BaseTest( object ):
    def setUp( self ):
        self.handler = adt.ArrayDatatype
        assert self.handler.isAccelerated
    def test_from_param( self ):
        p = self.handler.from_param( self.array )
        assert isinstance( p, ctypes.c_void_p )
    def test_dataPointer( self ):
        p = self.handler.dataPointer( self.array )
        assert isinstance( p, integer_types)
    def test_arraySize( self ):
        p = self.handler.arraySize( self.array )
        assert p == 6, p
    def test_arrayByteCount( self ):
        p = self.handler.arrayByteCount( self.array )
        assert p == 24, p
    def test_asArray( self ):
        p = self.handler.asArray( self.array )
        assert p is self.array 
    def test_unitSize( self ):
        p = self.handler.unitSize( self.array )
        assert p == 3, p
    def test_dimensions( self ):
        p = self.handler.dimensions( self.array )
        assert p == (2,3), p
    
    def test_arrayToGLType( self ):
        p = self.handler.arrayToGLType( self.array )
        assert p == GL.GL_FLOAT

if numpy:
    # Skip if modifies the functions, which are *shared* between the 
    # classes...
    #@pytest.mark.skipif( not numpy, reason="Numpy not available")
    class TestNumpy( _BaseTest, unittest.TestCase ):
        def setUp( self ):
            self.array = numpy.array( [[1,2,3],[4,5,6]],'f')
            super(TestNumpy,self).setUp()
        def test_dataPointer( self ):
            p = self.handler.dataPointer( self.array )
            assert isinstance( p, integer_types)
            assert p == self.array.ctypes.data
        def test_zeros( self ):
            p = self.handler.zeros( (2,3,4), 'f' )
            assert p.shape == (2,3,4)
            assert p.dtype == numpy.float32
        def test_asArrayConvert( self ):
            p = self.handler.asArray( self.array, GL.GL_DOUBLE )
            assert p is not self.array 
            assert p.dtype == numpy.float64
            p = self.handler.asArray( self.array, 'd' )
            assert p is not self.array 
            assert p.dtype == numpy.float64
        def test_zeros_typed( self ):
            z = self.handler.zeros( (2,3,4), GL.GL_FLOAT)
            assert z.shape == (2,3,4)
            assert z.dtype == numpy.float32
        def test_downconvert( self ):
            p = self.handler.asArray( numpy.array( [1,2,3],'d'), GL.GL_FLOAT )
            assert p.dtype == numpy.float32
        def test_zeros_small( self ):
            z = self.handler.zeros( 0, GL.GL_BYTE )
            assert z.dtype == numpy.byte, z

class TestVBO( _BaseTest, unittest.TestCase ):
    def setUp( self ):
        if numpy:
            self.array = vbo.VBO(numpy.array( [[1,2,3],[4,5,6]],'f'))
        else:
            self.array = vbo.VBO(adt.GLfloatArray.asArray([[1,2,3],[4,5,6]]))
        super(TestVBO,self).setUp()

class TestVBOOffset( _BaseTest, unittest.TestCase ):
    def setUp( self ):
        if numpy:
            self.array = vbo.VBO(numpy.array( [[1,2,3],[4,5,6]],'f')) + 12
        else:
            self.array = vbo.VBO(adt.GLfloatArray.asArray([[1,2,3],[4,5,6]])) + 12
        super(TestVBOOffset,self).setUp()
        
class TestNones( unittest.TestCase ):
    def setUp( self ):
        self.array = None
        self.handler = adt.ArrayDatatype
        assert self.handler.isAccelerated
    def test_from_param( self ):
        p = self.handler.from_param( self.array )
        assert p is None, p
    def test_dataPointer( self ):
        p = self.handler.dataPointer( self.array )
        assert p is None
    def test_asArray( self ):
        p = self.handler.asArray( self.array )
        assert p is self.array 
    def test_dimensions( self ):
        p = self.handler.dimensions( self.array )
        assert p == (0,), p
