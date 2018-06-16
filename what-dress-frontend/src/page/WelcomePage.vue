<template>
  <div v-loading="loading" element-loading-text="正在识别，请稍等">
    <div style="text-align:center;">
        <p style="font-size:14px; color:#797979; padding: 20px;">Tentcoo Dress AI 通过专业的时装数据集与神经网络识别技术，识别女生服装的类别属性。让广大"IT男"朋友，解决看不懂女生穿的什么衣服。</p>
        <el-upload
          class="upload-demo"
          drag
          action="./classify"
          
          :on-change="onProgress"   
          :on-success="onSuccess" 
          :on-error="onError" 
          :show-file-list="false"
          multiple>
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将需要识别的图片拖到此处，或<em>点击上传</em></div>
          <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div>
        </el-upload>
        <p style="font-size:10px; color:#797979; margin: 50px 15px;">&copy; Tentcoo Studio 2018 Designed by Steve Ou.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WelcomePage',
  methods:{
    onProgress(){
      this.$data.loading = true
    },
    onSuccess(response, file, fileList){
      this.$data.loading = false
      this.$router.push({
        name:"Result",
        params:{
          file:file,
          result:response
        }
      });
    },
    onError(){
      this.$data.loading = false
      this.$notify.error({
        title: '错误',
        message: '识别服务器出bug了,识别不出来,请刷新或稍后重试'
      });
    }
  },
  data: function () {
    return {
      loading: false
    }
  }
}
</script>
