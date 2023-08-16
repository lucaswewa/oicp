import os
import sys
import platform
import time
import numpy
import cv2

num = 3
os.environ["PYLON_CAMEMU"] = "%d" % num
from pypylon import pylon
from pypylon import genicam
from pypylon.pylon import InstantCamera

class ConfigurationEventPrinter(pylon.ConfigurationEventHandler):
    def OnAttach(self, camera):
        print("OnAttach event")

    def OnAttached(self, camera):
        print("OnAttached event for device ", camera.GetDeviceInfo().GetModelName())

    def OnOpen(self, camera):
        print("OnOpen event for device ", camera.GetDeviceInfo().GetModelName())

    def OnOpened(self, camera):
        print("OnOpened event for device ", camera.GetDeviceInfo().GetModelName())

    def OnGrabStart(self, camera):
        print("OnGrabStart event for device ", camera.GetDeviceInfo().GetModelName())

    def OnGrabStarted(self, camera):
        print("OnGrabStarted event for device ", camera.GetDeviceInfo().GetModelName())

    def OnGrabStop(self, camera):
        print("OnGrabStop event for device ", camera.GetDeviceInfo().GetModelName())

    def OnGrabStopped(self, camera):
        print("OnGrabStopped event for device ", camera.GetDeviceInfo().GetModelName())

    def OnClose(self, camera):
        print("OnClose event for device ", camera.GetDeviceInfo().GetModelName())

    def OnClosed(self, camera):
        print("OnClosed event for device ", camera.GetDeviceInfo().GetModelName())

    def OnDestroy(self, camera):
        print("OnDestroy event for device ", camera.GetDeviceInfo().GetModelName())

    def OnDestroyed(self, camera):
        print("OnDestroyed event")

    def OnDetach(self, camera):
        print("OnDetach event for device ", camera.GetDeviceInfo().GetModelName())

    def OnDetached(self, camera):
        print("OnDetached event for device ", camera.GetDeviceInfo().GetModelName())

    def OnGrabError(self, camera, errorMessage):
        print("OnGrabError event for device ", camera.GetDeviceInfo().GetModelName())
        print("Error Message: ", errorMessage)

    def OnCameraDeviceRemoved(self, camera):
        print("OnCameraDeviceRemoved event for device ", camera.GetDeviceInfo().GetModelName())

class CameraEventPrinter(pylon.CameraEventHandler):
    def OnCameraEvent(self, camera, userProvidedId, node):
        print("OnCameraEvent event for device ", camera.GetDeviceInfo().GetModelName())
        print("User provided ID: ", userProvidedId)
        print("Event data node name: ", node.GetName())
        value = genicam.CValuePtr(node)
        if value.IsValid():
            print("Event node data: ", value.ToString())
        print()

def get_class_and_filter():
    device_class = "BaslerCamEmu"
    di = pylon.DeviceInfo()
    di.SetDeviceClass(device_class)
    return device_class, [di]

num_dev = num
device_class, device_filter = get_class_and_filter()

def create_first():
    tlf = pylon.TlFactory.GetInstance()
    return pylon.InstantCamera(tlf.CreateFirstDevice(device_filter[0]))

# general
camera: InstantCamera = create_first()
camera.Open()
camera.ExposureTimeAbs.SetValue(10000.0)
exp_time_abs = camera.ExposureTimeAbs.GetValue()
result = camera.GrabOne(1000)
img = result.GetArray()
cv2.imwrite("test.png", img)
camera.Close()


# test call
print()
print("######## call.py ########")
camera.Open()
print(camera.GetSfncVersion)

camera.MaxNumBuffer.Value = 22
camera.GainRaw.Vallue = 192
print(camera.GainRaw.Value)

print(camera.MaxNumBuffer.Value)
camera.Close()

# test callback.py
print()
print("######## callback.py ########")
camera.Open()
print("using device", camera.GetDeviceInfo().GetModelName())

def callback(node):
    print("Callback", type(node))
    print("Callback", node.Node.Name)

genicam.Register(camera.GainRaw.Node, callback)

camera.GainRaw = camera.GainRaw.Max

camera.GainRaw = camera.GainRaw.Min

camera.Close()

# test grab.py
print()
print("######## grab.py ########")

# Number of images to be grabbed.
countOfImagesToGrab = 20

# The exit code of the sample application.
exitCode = 0

camera.Open()

try:

    new_width = camera.Width.GetValue() - camera.Width.GetInc()
    if new_width >= camera.Width.GetMin():
        camera.Width.SetValue(new_width)

    camera.MaxNumBuffer = 10

    camera.StartGrabbingMax(countOfImagesToGrab)

    while camera.IsGrabbing():
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

        if grabResult.GrabSucceeded():
            print("SizeX:", grabResult.Width)
            print("SizeY:", grabResult.Height)
            img = grabResult.Array
            print("Gray value of first pixel: ", img[0,0])
        else:
            print("Error: ", grabResult.ErrorCode, grabResult.ErrorDescription)
        grabResult.Release()

    camera.Close()
except genicam.GenericException as e:
    print("An exception occurred.")
    print(e.GetDescription())
    exitCode = 1

print("exit code: ", exitCode)


# test grabcameraevents.py
print()
print("######## grabcameraevents.py ########")

eMyExposureEndEvent = 100

# Number of images to be grabbed.
countOfImagesToGrab = 5


# Example handler for camera events.
class SampleCameraEventHandler(pylon.CameraEventHandler):
    # Only very short processing tasks should be performed by this method. Otherwise, the event notification will block the
    # processing of images.
    def OnCameraEvent(self, camera, userProvidedId, node):
        print()
        if userProvidedId == eMyExposureEndEvent:
            print("Exposure End event. FrameID: ", camera.EventExposureEndFrameID.Value, " Timestamp: ",
                  camera.EventExposureEndTimestamp.Value)
            # More events can be added here.


# Example of an image event handler.
class SampleImageEventHandler(pylon.ImageEventHandler):
    def OnImageGrabbed(self, camera, grabResult):
        print("CSampleImageEventHandler.OnImageGrabbed called.")
        print()
        print()

exitCode = 0
handler1 = SampleCameraEventHandler()
handler2 = CameraEventPrinter()

try:
    camera = create_first()

    # camera.RegisterConfiguration(pylon.SoftwareTriggerConfiguration(), pylon.RegistrationMode_ReplaceAll, pylon.Cleanup_Delete)
    # camera.RegisterConfiguration(ConfigurationEventPrinter(), pylon.RegistrationMode_Append, pylon.Cleanup_Delete)
    # camera.RegisterImageEventHandler(SampleImageEventHandler(), pylon.RegistrationMode_Append, pylon.Cleanup_None)
    # camera.GrabCameraEvents = True
    # camera.RegisterCameraEventHandler(handler2, "EventExposureEndFrameID", eMyExposureEndEvent, pylon.RegistrationMode_Append, pylon.Cleanup_None)
    # camera.RegisterCameraEventHandler(handler2, "EventExposureEndTimestamp", eMyExposureEndEvent, pylon.RegistrationMode_Append, pylon.Cleanup_None)

    camera.Open()

    if not genicam.IsAvailable(camera.EventSelector):
        raise genicam.RuntimeException("The device doesn't support events.")
    
    camera.EventSelector = "ExposureEnd"
    camera.EventNotification = "On"
    camera.StartGrabbingMax(countOfImagesToGrab)

    while camera.IsGrabbing():
        if camera.WaitForFrameTriggerReady(1000, pylon.TimeoutHandling_ThrowException):
            camera.ExecuteSoftwareTrigger()

        grabResult = camera.RetrieveResult(5000)

    camera.EventSelector = "ExposureEnd"
    camera.EventNotification = "Off"
except genicam.GenericException as e:
    print("An exception occurred.")

camera.Close()

# test grabmultiplecameras.py
print()
print("######## grabmultiplecameras.py ########")

# Number of images to be grabbed.
countOfImagesToGrab = 10

# Limits the amount of cameras used for grabbing.
# It is important to manage the available bandwidth when grabbing with multiple cameras.
# This applies, for instance, if two GigE cameras are connected to the same network adapter via a switch.
# To manage the bandwidth, the GevSCPD interpacket delay parameter and the GevSCFTD transmission delay
# parameter can be set for each GigE camera device.
# The "Controlling Packet Transmission Timing with the Interpacket and Frame Transmission Delays on Basler GigE Vision Cameras"
# Application Notes (AW000649xx000)
# provide more information about this topic.
# The bandwidth used by a FireWire camera device can be limited by adjusting the packet size.
maxCamerasToUse = 2

# The exit code of the sample application.
exitCode = 0

try:
    tlFactory = pylon.TlFactory.GetInstance()
    devices = tlFactory.EnumerateDevices()
    if len(devices) == 0:
        raise pylon.RuntimeException("No camera present.")
    
    cameras = pylon.InstantCameraArray(min(len(devices), maxCamerasToUse))
    l = cameras.GetSize()

    for i, cam in enumerate(cameras):
        cam.Attach(tlFactory.CreateDevice(devices[i]))
        print("Using device ", cam.GetDeviceInfo().GetModelName())

    cameras.StartGrabbing()

    for i in range(countOfImagesToGrab):
        if not cameras.IsGrabbing():
            break

        grabResult = cameras.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        cameraContextValue = grabResult.GetCameraContext()
        print("Camera ", cameraContextValue, ": ", cameras[cameraContextValue].GetDeviceInfo().GetModelName())

        print("GrabSucceeded:", grabResult.GrabSucceeded())
        print("SizeX:", grabResult.GetWidth())
        print("SizeY:", grabResult.GetHeight())
        img = grabResult.GetArray()
        print("Gray value of first pixel: ", img[0,0])
except genicam.GenericException as e:
    print("An exception occurred.", e.GetDescription())
    exitCode = 1
cameras.Close()

# test grabone.py
print()
print("######## grabone.py ########")

camera = create_first()

camera.Open()
# camera.ChunkModeActive = True

# for cf in camera.ChunkSelector.Symbolics:
#     camera.ChunkSelector = cf
#     camera.ChunkEnable = True

result = camera.GrabOne(100)
print("Mean Gray value:", numpy.mean(result.Array[0:20, 0]))

# def ChunksOnResult(result):
#     ret = ""
#     for f in camera.ChunkSelector.Symbolics:
#         try:
#             if genicam.IsAvailable(getattr(result, "Chunk" + f)):
#                 ret += f + ","
#         except AttributeError as e:
#             # some cameras have chunkselectors which never occur in the video stream
#             print(e)
#     return ret


# print(ChunksOnResult(result))

camera.Close()

# test grabstrategies.py
print()
print("######## grabstrategies.py ########")

# test grabusinggrabloopthread.py
print()
print("######## grabusinggrabloopthread.py ########")

# test helloworld.py
print()
print("######## helloworld.py ########")

# test ifacenodemap_pocxp.py
print()
print("######## ifacenodemap_pocxp.py ########")

# test opencv.py
print()
print("######## opencv.py ########")

camera = create_first()
# Grabing Continusely (video) with minimal delay
camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
converter = pylon.ImageFormatConverter()

# converting to opencv bgr format
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

while camera.IsGrabbing():
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

    if grabResult.GrabSucceeded():
        # Access the image data
        image = converter.Convert(grabResult)
        img = image.GetArray()
        cv2.namedWindow('title', cv2.WINDOW_NORMAL)
        cv2.imshow('title', img)
        k = cv2.waitKey(1)
        if k == 27:
            break
    grabResult.Release()
    
# Releasing the resource    
camera.StopGrabbing()

cv2.destroyAllWindows()

# test parametrizecameraloadandsaveconfig.py
print()
print("######## parametrizecameraloadandsaveconfig.py ########")

# The name of the pylon file handle
nodeFile = "NodeMap.pfs"

# Create an instant camera object with the camera device found first.
camera = create_first()
camera.Open()
# Print the model name of the camera.
print("Using device ", camera.GetDeviceInfo().GetModelName())

# featurePersistence = pylon.FeaturePersistence()

print("Saving camera's node map to file...")
print(nodeFile)

# Save the content of the camera's node map into the file.
pylon.FeaturePersistence.Save(nodeFile, camera.GetNodeMap())

# Just for demonstration, read the content of the file back to the camera's node map with enabled validation.
print("Reading file back to camera's node map...")
pylon.FeaturePersistence.Load(nodeFile, camera.GetNodeMap(), True)
# Close the camera.
camera.Close()

# test save_image.py
print()
print("######## save_image.py ########")

num_img_to_save = 5
img = pylon.PylonImage()
tlf = pylon.TlFactory.GetInstance()

cam = pylon.InstantCamera(tlf.CreateFirstDevice())
cam.Open()
cam.StartGrabbing()
for i in range(num_img_to_save):
    with cam.RetrieveResult(2000) as result:

        # Calling AttachGrabResultBuffer creates another reference to the
        # grab result buffer. This prevents the buffer's reuse for grabbing.
        img.AttachGrabResultBuffer(result)

        if platform.system() == 'Windows':
            # The JPEG format that is used here supports adjusting the image
            # quality (100 -> best quality, 0 -> poor quality).
            ipo = pylon.ImagePersistenceOptions()
            quality = 90 - i * 10
            ipo.SetQuality(quality)

            filename = "saved_pypylon_img_%d.jpeg" % quality
            img.Save(pylon.ImageFileFormat_Jpeg, filename, ipo)
        else:
            filename = "saved_pypylon_img_%d.png" % i
            img.Save(pylon.ImageFileFormat_Png, filename)

        # In order to make it possible to reuse the grab result for grabbing
        # again, we have to release the image (effectively emptying the
        # image object).
        img.Release()

cam.StopGrabbing()
cam.Close()

# test startup.py
print()
print("######## startup.py ########")

IMAGES_TO_GRAB = 50
exitCode = 0

camera = pylon.InstantCamera(
    pylon.TlFactory.GetInstance().CreateFirstDevice())

camera.Open()

# Print the model name of the camera.
print("Using device ", camera.GetDeviceInfo().GetModelName())

camera.MaxNumBuffer = 2
try:
    camera.Gain = camera.Gain.Max
except genicam.LogicalErrorException:
    camera.GainRaw = camera.GainRaw.Max
camera.Width = camera.Width.Max
camera.Height = camera.Height.Max
# camera.ExposureTime = camera.ExposureTime.Min
camera.PixelFormat = "Mono8"

# Start the grabbing of IMAGES_TO_GRAB images.
# The camera device is parameterized with a default configuration which
# sets up free-running continuous acquisition.
camera.StartGrabbingMax(IMAGES_TO_GRAB)

# Camera.StopGrabbing() is called automatically by the RetrieveResult() method
# when IMAGES_TO_GRAB images have been retrieved.
try:
    while camera.IsGrabbing():
        result = camera.RetrieveResult(
            5000,
            pylon.TimeoutHandling_ThrowException)
        print(result.GrabSucceeded())
        # Image grabbed successfully?
        if result.GrabSucceeded():
            # Access the image data.
            print("SizeX: ", result.Width)
            print("SizeY: ", result.Height)
            print(pylon.IsPacked(result.PixelType))
            print("Mean Gray value:", numpy.mean(result.Array[0:20, 0]))
            # Display the grabbed image.
            # pylon.DisplayImage(1, result)
            result.Release()

        else:
            print("Error: ", result.GetErrorCode(), result.GetErrorDescription())

except genicam.GenericException as e:
    # Error handling.
    print("An exception occurred.", e.GetDescription())

camera.Close()
    
# test utilityimageformatconverter.py
print()
print("######## utilityimageformatconverter.py ########")

# This is a helper function for showing an image on the screen if Windows is used,
# and for printing the first bytes of the image.
def show_image(image, message):
    print(message)
    pBytes = image.Array
    print("Bytes of the image: \n")
    print(pBytes)


try:
    # Create the converter and set parameters.
    converter = pylon.ImageFormatConverter()
    converter.OutputPixelFormat = pylon.PixelType_RGB8packed
    converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

    # Try to get a grab result for demonstration purposes.
    print("Waiting for an image to be grabbed.")
    try:
        camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        grabResult = camera.GrabOne(1000)
        show_image(grabResult, "Grabbed image.")
        targetImage = pylon.PylonImage.Create(pylon.PixelType_Mono8, grabResult.GetWidth(), grabResult.GetHeight());
        print(converter.IsSupportedOutputFormat(pylon.PixelType_Mono8))
        # Now we can check if conversion is required.
        if converter.ImageHasDestinationFormat(grabResult):
            # No conversion is needed. It can be skipped for saving processing
            # time.
            show_image(grabResult, "Grabbed image.")

        else:
            # Conversion is needed.
            show_image(grabResult, "Grabbed image.")
            targetImage=converter.Convert(grabResult)
            show_image(targetImage, "Converted image.")
            filename = "saved_pypylon_converted.png"
            targetImage.Save(pylon.ImageFileFormat_Png, filename)

    except genicam.GenericException as e:
        print("Could not grab an image: ", e.GetDescription())
except genicam.GenericException as e:
    print("An exception occurred. ", e.GetDescription())


# test utilityimageformatconverter1.py
print()
print("######## utilityimageformatconverter1.py ########")

def show_image(img, message):
    print(message)

    image_array = img.GetArray()
    print(image_array)



def grab_image():
    try:
        camera = pylon.InstantCamera(
            pylon.TlFactory.GetInstance().CreateFirstDevice())

        camera.Open()
        result = camera.GrabOne(100)
        camera.Close()
        return result
    except genicam.GenericException as e:
        print("Could not grab an image: ", e.GetDescription())


try:
    # The image format converter basics.
    # First the image format converter class must be created.
    converter = pylon.ImageFormatConverter()

    # Second the converter must be parameterized.
    converter.OutputPixelFormat = pylon.PixelType_Mono16
    converter.OutputBitAlignment = "MsbAligned"
    # or alternatively
    converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned


    # Then it can be used to convert input images to
    # the target image format.

    # Grab an image
    image = grab_image()
    show_image(image, "Source Image")

    # Now we can check if conversion is required.
    if (converter.ImageHasDestinationFormat(image)):
        show_image(image, "No conversion needed.")
    else:
        # Convert the image. Note that there are more overloaded Convert methods avilable, e.g.
        # for converting the image from or to a user buffer.
        target_image = converter.Convert(image)
        show_image(target_image, "Converted image.")
except genicam.GenericException as e:
    print("An exception occurred. ", e.GetDescription())


# test zerocopy.py
print()
print("######## zerocopy.py ########")

"""This sample shows how some time can be saved by accessing the image buffer
without copying its contents. Keep in mind that while a zero-copy array has a
reference to the image buffer, this buffer cannot be released and cannot be
reused for grabbing.
"""

cam = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
cam.Open()
print("camera model: %s" % cam.DeviceModelName.GetValue())
print("AOI: %d x %d" % (cam.Width.GetValue(), cam.Height.GetValue()))
print("payload size: %d\n" % cam.PayloadSize.GetValue())

pxl_sum = 0
time_zc = 0
count_zc = 0
time_cpy = 0
count_cpy = 0
cam.StartGrabbing(pylon.GrabStrategy_OneByOne)

deadline = time.perf_counter() + 10
print("Using zero copy for 10 seconds.")
while time.perf_counter() < deadline:
    with cam.RetrieveResult(1000) as result:
        start = time.perf_counter()
        with result.GetArrayZeroCopy() as zc:
            pxl_sum += zc[0, 0]
        time_zc += time.perf_counter() - start
    count_zc += 1

deadline = time.perf_counter() + 10
print("Using copy for 10 seconds.")
while time.perf_counter() < deadline:
    with cam.RetrieveResult(1000) as result:
        start = time.perf_counter()
        pxl_sum += result.GetArray()[0, 0]
        time_cpy += time.perf_counter() - start
    count_cpy += 1

cam.StopGrabbing()
cam.Close()


print(
    " zc: %.3g s,  %d images, %.3g s / per image" %
    (time_zc, count_zc, time_zc / count_zc)
    )
print(
    "cpy: %.3g s,  %d images, %.3g s / per image" %
    (time_cpy, count_cpy, time_cpy / count_cpy)
    )
ratio = (time_cpy * count_zc) / (time_zc * count_cpy)
print("zero copy is %.1f times faster" % ratio)