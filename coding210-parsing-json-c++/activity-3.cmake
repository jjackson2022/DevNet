
project(coding210_parsing_json_cpp_activity_3)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")



# main-http
set(SOURCE_FILES
    main-json.cpp)

add_executable(coding210_3_main_json ${SOURCE_FILES})
target_link_libraries(coding210_3_main_json curl)


