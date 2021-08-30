CXXFLAGS = -I include  -std=c++11 -O3 $(shell python3.8-config --cflags)
LDFLAGS = $(shell python3.8-config --ldflags)

DEPS = lanmslib.h $(shell find include -xtype f)
CXX_SOURCES = lanmslib.cpp include/clipper/clipper.cpp

LIB_SO = build/lanmslib.so

$(LIB_SO): $(CXX_SOURCES) $(DEPS)
	$(CXX) -o $@ $(CXXFLAGS) $(LDFLAGS) $(CXX_SOURCES) --shared -fPIC

clean:
	rm -rf $(LIB_SO)
