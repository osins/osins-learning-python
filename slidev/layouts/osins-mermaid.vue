<!-- default.vue -->
<template>
  <div class="osins-mermaid">
    <slot />
  </div>
</template>

<style lang="less">
  body {
    font-family: 'Roboto', sans-serif;
  }

  #app,#page-root,.slide-container,.slideshow,.slide-content{
    border-width: 0px;
    width: 100% !important;
  }

  .osins-mermaid{
    padding: 10px;
    font-size: 9px !important;
    line-height: 1.2;
    overflow:scroll;
    h1,h2{
      font-size: 24px;
      margin-bottom: 10px;
    }
    .mermaid{
      margin: auto;
      font-size: 12px;
    }
  }
</style>