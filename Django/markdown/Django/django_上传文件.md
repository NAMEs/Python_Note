# request.FILES
	- 一个字典
	- django在文件上传期间，实际文件数据存储在request.FILES中。
	- 这个字典中的每个条目都是一个UploadedFile对象

# class UploadedFIle
	- 常用方法：
		- UploadedFile.read()	读取上传文件的所有数据（到内存），小心使用如果文件过大，会导致内存出现问题
		- UploadedFile.chunks 	生成器返回文件块，通常配合for循环使用

	- 常用属性：
		- UploadedFile.name 	文件名
		- UploadedFile.size 	文件大小
		- UploadedFile.content_type 	文件类型
		- UploadedFile.content_type_extra
		- UploadedFile.charset 	文件字符集